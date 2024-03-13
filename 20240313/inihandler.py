###############################################################################
# File: inihandler.py
# Author: Johannes Humann
# Created: February, 2024
# Origin: Foxpro-inihandler from w00dy
#
# Description:
# the inihandler is a class to produce and read structured ini-files
# for configuration of software.
# with a good structure, these files are more readable and maintainable
#
# Example:
# handler.write("System", "host", "127.0.0.1")
# handler.write("System", "port", "5500")
# handler.write("User", "name", "MyName")
# handler.write("User", "key", "12345")
#
# Result File:
# [System]
# host = 127.0.0.1
# port = 5500

# [User]
# name = MyName
# key = 12345
###############################################################################
import configparser
from pathlib import Path


class IniHandler:
    def __init__(self, filename):
        self._inifile = filename
        self._parser = configparser.ConfigParser()
        path = Path(self._inifile)

        if not path.exists():
            path.touch()

        self._parser.read(filename)

    def read(self, section, key, default=None):
        if self._parser.has_option(section, key):
            return self._parser.get(section, key)
        else:
            if default:
                self.write(section, key, default)

            return default

    def write(self, section, key, value):
        if not self._parser.has_section(section):
            self._parser.add_section(section)
        self._parser.set(section, key, value)
        with open(self._inifile, "w") as configfile:
            self._parser.write(configfile)
        return True

    def readsection(self):
        return ";".join(self._parser.sections())

    def delesection(self, section):
        if self._parser.has_section(section):
            self._parser.remove_section(section)
            with open(self._inifile, "w") as configfile:
                self._parser.write(configfile)
            return True
        return False

    def readkeys(self, section):
        if self._parser.has_section(section):
            return ";".join(self._parser.options(section))
        return ""

    def readentries(self, section):
        if self._parser.has_section(section):
            return ";".join(
                [f"{key}={value}"
                 for key, value
                 in self._parser.items(section)]
            )
        return ""

    def deletekey(self, section, key):
        if (self._parser.has_section(section) and
                self._parser.has_option(section, key)):
            self._parser.remove_option(section, key)
            with open(self._inifile, "w") as configfile:
                self._parser.write(configfile)
            return True
        return False
