#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class ConfigStore(object, metaclass=Singleton):
    config = {}  # read user configuration as-is
    config2 = {}  # store converted strings and numbers as objects
