#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import services

from dynamic_interactions.init import Init
from dynamic_interactions.modinfo import ModInfo

from sims.sim import Sim
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.common_enums.vanilla_regions import VanillaRegions
from ts4lib.common_enums.vanilla_venues import VanillaVenues
from ts4lib.utils.vanilla_names import VanillaNames
from ts4lib.utils.worlds_and_neighbourhoods import WorldsAndNeighbourhoods

mod_name = ModInfo.get_identity().name
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class Cheats:
    # noinspection PyUnusedLocal
    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.dynint.init', '...', )
    def o19_cheat_init_dynamic_interactions(output: CommonConsoleCommandOutput):
        i = Init()
        i.modify_interactions()
        output(f"OK")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.dynint.info', '...', )
    def o19_cheat_init_dynamic_interactions(output: CommonConsoleCommandOutput):
        try:
            sim: Sim = CommonSimUtils.get_active_sim()
            output(f"Sim: {sim}")
            log.debug(f"Sim: {sim}")

            world_id = CommonLocationUtils().get_current_world_id()
            w, n = WorldsAndNeighbourhoods().get_world_and_neighbourhood_name(world_id)
            output(f"World/NH (id): {w} >> {n} ({world_id})")
            log.debug(f"World/NH (id): {w} >> {n} ({world_id})")

            region_id = getattr(services.current_region(), 'guid64', 0)
            output(f"Region: {VanillaRegions(region_id)})")
            log.debug(f"Region: {VanillaRegions(region_id)})")
            # r = VanillaNames.get(VanillaRegions(region_id))
            # output(f"{r} ({region_id})")
            # log.debug(f"{r} ({region_id})")

            venue_id = getattr(services.get_current_venue(), 'guid64', 0)
            output(f"Venue: {VanillaVenues(region_id)})")
            log.debug(f"Venue: {VanillaVenues(region_id)})")
            # r = VanillaNames.get(VanillaVenues(venue_id))
            # output(f"{r} ({venue_id})")
            # log.debug(f"{r} ({venue_id})")

            location = getattr(sim, 'location', None)
            if location:
                zone_id = getattr(location, 'zone_id', 0)
                output(f"zone_id: {zone_id}")
                log.debug(f"zone_id: {zone_id}")
                level = getattr(object, 'level', 0)
                output(f"level: {level}")
                log.debug(f"level: {level}")
                transform = getattr(location, 'transform', None)
                if transform:
                    position = getattr(transform, 'translation', None)
                    orientation = getattr(transform, 'orientation', None)
                    if position:
                        output(f"p/q: {position}/{orientation}")
                        log.debug(f"p/q: {position}/{orientation}")
                        block_id = CommonLocationUtils().get_block_id(services.current_zone_id(), position, level)
                        output(f"block_id: {block_id}")
                        log.debug(f"block_id: {block_id}")
        except Exception as e:
            output(f"Error {e}")
