#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Tuple, Set

from dynamic_interactions.config_store import ConfigStore
# noinspection PyUnresolvedReferences
from sims4.math import Vector3, Quaternion, Transform, Location

import services
from dynamic_interactions.modinfo import ModInfo
from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.utils.singleton import Singleton


mod_name = ModInfo.get_identity().name
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class Replace(object, metaclass=Singleton):
    def modify_interactions(self, game_object, add_interactions: Tuple = None, remove_interactions: Tuple = None):
        super_affordances: Set = set(self.get_super_affordances(game_object))
        if remove_interactions:
            super_affordances = set(super_affordance for super_affordance in super_affordances if getattr(super_affordance, 'guid64', 0) not in remove_interactions)
        if add_interactions:
            super_affordances.update(set(add_interactions))
        _super_affordances = tuple(super_affordances)
        self.set_super_affordances(game_object, _super_affordances)

    def apply_modifications(self):
        for _id, _config in ConfigStore.config.items():
            _config2 = ConfigStore.config2.get(_id, None)
            log.debug(f"Processing '{_id}':")
            if _config2 is None:
                continue

            add_interactions = _config2.get('add_interactions', set())
            remove_interactions = _config.get('remove_interactions', set())
            _filter = _config.get('filter', None)
            objects = _config2.get('objects', set())
            filter_objects = _config2.get('filter_objects', set())
            if _filter is None:
                # apply all changes without thinking
                for game_object in objects:
                    self.modify_interactions(game_object, add_interactions, remove_interactions)
                    log.debug(f"\tmodified {game_object} (no filter)")
            else:
                # check the _filter
                invert = _filter.get('invert', False)
                world_ids = _filter.get('world_ids', None)
                if world_ids:
                    world_id = CommonLocationUtils().get_current_world_id()
                    if invert:
                        if world_id in world_ids:
                            log.debug(f"Skipping world_id {world_id}")
                            continue
                    else:
                        if world_id not in world_ids:
                            log.debug(f"Skipping world_id {world_id}")
                            continue

                lot_ids = _filter.get('lot_ids', None)
                if lot_ids:
                    lot_id = CommonLocationUtils().get_current_lot_id()
                    if invert:
                        if lot_id in lot_ids:
                            log.debug(f"Skipping lot_id {lot_id}")
                            continue
                    else:
                        if lot_id not in lot_ids:
                            log.debug(f"Skipping lot_id {lot_id}")
                            continue

                venue_ids = _filter.get('venue_ids', None)
                if venue_ids:
                    venue_id = getattr(services.get_current_venue(), 'guid64', 0)
                    if invert:
                        if venue_id in venue_ids:
                            log.debug(f"Skipping venue_id {venue_id}")
                            continue
                    else:
                        if venue_id not in venue_ids:
                            log.debug(f"Skipping venue_id {venue_id}")
                            continue

                region_ids = _filter.get('region_ids', None)
                if region_ids:
                    region_id = getattr(services.current_region(), 'guid64', 0)
                    if invert:
                        if region_id in region_ids:
                            log.debug(f"Skipping lot_id {region_id}")
                            continue
                    else:
                        if region_id not in region_ids:
                            log.debug(f"Skipping lot_id {region_id}")
                            continue

                __objects = _filter.get('objects', None)  # objects are defined in config.id.objects,
                if invert:
                    if __objects and filter_objects:  # so they must not be in config2.id.filter_objects
                        log.debug(f"Skipping - objects found")
                        continue
                else:
                    if __objects and not filter_objects:  # so they must be also in config2.id.filter_objects
                        log.debug(f"Skipping - no objects found")
                        continue
                same_block = _filter.get('same_block', False)
                if same_block is True:
                    pass  # loop over objects and locate block_id and test them with all filter_objects
                    for _object in objects:
                        block_id = self.get_block_id(_object)
                        for _filter_object in filter_objects:
                            filter_block_id = self.get_block_id(_filter_object)
                            if invert:
                                if block_id != filter_block_id:
                                    self.modify_interactions(_object, add_interactions, remove_interactions)
                                    log.debug(f"\tmodified {_object} : {block_id} vs. {filter_block_id} : {_filter_object}")
                                    continue
                            else:
                                if block_id == filter_block_id:
                                    self.modify_interactions(_object, add_interactions, remove_interactions)
                                    log.debug(f"\tmodified {_object} : {block_id} vs. {filter_block_id} : {_filter_object}")
                                    continue
                            log.debug(f"\tpass {_object} : {block_id} vs. {filter_block_id} : {_filter_object}")

                else:  # loop over objects and modify tunings without further checks
                    for _object in objects:
                        self.modify_interactions(_object, add_interactions, remove_interactions)
                        log.debug(f"\tmodified {_object}")

    def get_block_id(self, game_object):
        location = getattr(game_object, '_location', None)
        if location:
            level = getattr(game_object, 'level', 0)
            zone_id = getattr(location, 'zone_id', 0)
            transform = getattr(location, 'transform', None)
            if transform:
                position = getattr(transform, 'translation', Vector3(0, 0, 0))
                parent_object = getattr(location, 'parent', None)
                if parent_object:
                    parent_location = getattr(parent_object, '_location', None)
                    if parent_location:
                        parent_transform = getattr(parent_location, 'transform', None)
                        if parent_transform:
                            parent_position = getattr(parent_transform, 'translation', Vector3(0, 0, 0))
                            position += parent_position
            else:
                position = Vector3(0, 0, 0)
        else:
            position = Vector3(0, 0, 0)
            level = 0
            try:
                zone_id = services.current_zone_id()
            except:
                zone_id = 0

        return CommonLocationUtils().get_block_id(zone_id, position, level)

    def get_super_affordances(self, interaction_target):
        if getattr(interaction_target, 'cp_super_affordances', None) is None:
            setattr(interaction_target, 'cp_super_affordances', getattr(interaction_target, '_super_affordances'))
        return getattr(interaction_target, '_super_affordances')

    def set_super_affordances(self, interaction_target, super_affordances):
        setattr(interaction_target, '_super_affordances', super_affordances)

    def restore_super_affordances(self, interaction_target):
        if getattr(interaction_target, 'cp_super_affordances', None) is not None:
            setattr(interaction_target, '_super_affordances', getattr(interaction_target, 'cp_super_affordances'))
