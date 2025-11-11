#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import ast
import os
from typing import Dict

import services
from sims4.resources import Types as ResourceType
from dynamic_interactions.config_store import ConfigStore
from dynamic_interactions.modinfo import ModInfo
# noinspection PyProtectedMember
from server_commands.object_commands import _all_objects_gen
from ts4lib.libraries.file_utils import FileUtils
from ts4lib.libraries.ts4folders import TS4Folders
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.utils.singleton import Singleton

mod_name = ModInfo.get_identity().name
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class UserConfig(object, metaclass=Singleton):
    def __init__(self):
        self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
        self.config_folder = os.path.join(self.ts4f.data_folder, 'cfg')
        self.fu = FileUtils(os.path.join(self.config_folder))

    def merge_configuration_files(self) -> Dict:
        rv: Dict = {}
        files = self.fu.find_files(r'^.*\.txt$')
        for file in files:
            try:
                with open(file, mode='rt', encoding='UTF-8') as fp:
                    data = ast.literal_eval(fp.read())
                    rv.update(data)
            except Exception as e:
                log.warn(f"Skipping file '{file}' with error '{e}'.")

        return rv

    def read_configuration(self):
        """
        1. Read all configuration files from `The Sims 4/mod_data/dynamic_interactions/cfg/*.txt`
        2. Populate ConfigStore.config2 with values from ConfigStore.config
        """
        ConfigStore.config2 = {}
        ConfigStore.config = self.merge_configuration_files()

        manager = services.object_manager()
        lot_filter = None
        for o in _all_objects_gen(manager, lot_filter):
            try:
                game_object: o = manager.get(o.id)
                object_tags = game_object.get_tags()
                object_name: str = type(o).__name__
                self._add_object_to_config(game_object, object_tags, object_name)
            except Exception as e:
                log.error(f"FATAL: {e}")
                return
        self._add_interactions_to_config()
        log.debug(f"merged configuration files() -> {ConfigStore.config}")
        log.debug(f"merged configuration files() -> {ConfigStore.config2}")

    def _add_object_to_config(self, game_object, object_tags, object_name):
        log.debug(f"_add_object_to_config(, {game_object}, {object_tags}, {object_name})")
        for _id, _config in ConfigStore.config.items():
            _config2 = ConfigStore.config2.get(_id, {})
            s_found = False
            f_found = False

            if object_tags:
                s_tags = _config.get('objects', {}).get('tags', set())
                for s_tag in s_tags:
                    if s_tag in object_tags:
                        log.debug(f"\tfound '{_id}' s (tag): '{game_object}")
                        s_objects = _config2.get('objects', set())
                        s_objects.add(game_object)
                        _config2.reset_motives({'objects': s_objects})
                        s_found = True
                        break
                f_tags = _config.get('filter', {}).get('objects', {}).get('tags', set())
                for f_tag in f_tags:
                    if f_tag in object_tags:
                        log.debug(f"\tfound '{_id}' f (tag): '{game_object}")
                        f_objects = _config2.get('filter_objects', set())
                        f_objects.add(game_object)
                        _config2.reset_motives({'filter_objects': f_objects})
                        f_found = True
                        break

            if object_name:
                if not s_found:
                    s_names = _config.get('objects', {}).get('names', set())
                    if object_name in s_names:
                        log.debug(f"\tfound '{_id}' s (name): '{game_object}")
                        s_objects = _config2.get('objects', set())
                        s_objects.add(game_object)
                        _config2.reset_motives({'objects': s_objects})
                        s_found = True

                if not f_found:
                    f_names = _config.get('filter', {}).get('objects', {}).get('names', set())
                    if object_name in f_names:
                        log.debug(f"\tfound '{_id}' f (name): '{game_object}")
                        f_objects = _config2.get('filter_objects', set())
                        f_objects.add(game_object)
                        _config2.reset_motives({'filter_objects': f_objects})
                        f_found = True
            if s_found or f_found:
                ConfigStore.config2.reset_motives({_id: _config2})

    def _add_interactions_to_config(self):
        interaction_manager = services.get_instance_manager(ResourceType.INTERACTION)
        for _id, _config in ConfigStore.config.items():
            _config2 = ConfigStore.config2.get(_id, {})
            for _interactions in ('add_interactions', ):  # 'remove_interactions', ):
                interaction_ids = _config.get(_interactions, None)
                if interaction_ids:
                    __interactions = set()
                    for interaction_id in interaction_ids:
                        interaction_instance = interaction_manager.get(interaction_id)
                        __interactions.add(interaction_instance)
                    _config2.reset_motives({_interactions: __interactions})
                    ConfigStore.config2.reset_motives({_id: _config2})
