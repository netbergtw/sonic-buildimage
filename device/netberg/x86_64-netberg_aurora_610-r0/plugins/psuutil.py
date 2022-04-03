#
# psuutil.py
# Platform-specific PSU status interface for SONiC
#


import os.path

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")


class PsuUtil(PsuBase):
    """Platform-specific PSUutil class"""

    def __init__(self):
        PsuBase.__init__(self)

    def get_num_psus(self):
        return 2

    def get_psu_status(self, index):
        if index == 1:
            psu_path = "/sys/bus/i2c/devices/0-0077/psu0"
        elif index == 2:
            psu_path = "/sys/bus/i2c/devices/0-0077/psu1"
        else:
            return False

        try:
            data = open(psu_path, "rb")
        except IOError:
            return False

        result = int(data.read(1).encode("hex"), 16)
        data.close()
        if result == 48:
            return True
        else:
            return False

    def get_psu_presence(self, index):
        if index == 1:
            psu_path = "/sys/bus/i2c/devices/0-0077/psu0"
        elif index == 2:
            psu_path = "/sys/bus/i2c/devices/0-0077/psu1"
        else:
            return False

        try:
            data = open(psu_path, "rb")
        except IOError:
            return False

        result = int(data.read(1).encode("hex"), 16)
        data.close()

        if result == 48:
            return True
        else:
            return False
