from configparser import ConfigParser

"""
Return the value from config file
Param:FileLocation,Config_Section,Config_key
Return: Config value in String
"""

config = ConfigParser()
config.read(r"../data/config.ini")

class ReadConfig:

    @staticmethod
    def read_config(section, key):
        value = config.get(section, key)
        return value

