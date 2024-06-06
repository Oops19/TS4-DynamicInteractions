#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import os

from dynamic_interactions.modinfo import ModInfo
from dynamic_interactions.replace import Replace
from dynamic_interactions.user_config import UserConfig
from sims4communitylib.events.build_buy.events.build_buy_exit import S4CLBuildBuyExitEvent
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from ts4lib.libraries.ts4folders import TS4Folders
from ts4lib.utils.singleton import Singleton
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


mod_name = ModInfo.get_identity().name
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name, custom_file_path=None)
log.enable()
log.info(f"Thank you for using Dynamic Interactions!")


class Init(object, metaclass=Singleton):

    def __init__(self):
        try:
            self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
            self.tunings_folder = os.path.join(self.ts4f.data_folder, 'tunings')
            self.uc = UserConfig()
            self.rt = Replace()
            log.info(f"Dynamic Interactions initialized.")
        except:
            log.error(f"Could not initialize Dynamic Interactions!", throw=True)

    def modify_interactions(self):
        self.uc.read_configuration()
        self.rt.apply_modifications()

    # noinspection PyUnusedLocal
    @staticmethod
    @CommonEventRegistry.handle_events(f"{mod_name}_zone")
    def zone_loaded(event_data: S4CLZoneLateLoadEvent):
        i = Init()
        i.modify_interactions()

    # noinspection PyUnusedLocal
    @staticmethod
    @CommonEventRegistry.handle_events(f"{mod_name}_buy")
    def zone_loaded(event_data: S4CLBuildBuyExitEvent):
        i = Init()
        i.modify_interactions()
