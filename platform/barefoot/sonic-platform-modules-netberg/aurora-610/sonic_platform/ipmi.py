#!/usr/bin/env python

try:
    from subprocess import Popen, PIPE
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

class Ipmi():
    def get_bmc_version(self):
        bmc_version=None
        target="Firmware Revision"

        output = Popen(["ipmitool","mc","info"], stdout=PIPE)
        ret_str=output.communicate()[0]
        start_idx=ret_str.find(target)
        start_idx+=len(target)
        offset=ret_str[start_idx:].find('\n')
        end_idx=start_idx+offset

        bmc_version=ret_str[start_idx:end_idx]
        bmc_version=bmc_version.replace(":"," ")
        bmc_version=bmc_version.strip()

        return bmc_version