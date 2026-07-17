#!/bin/bash
/sbin/modprobe -a nb_platform nb_ports_ioctl nb_leds_ioctl nb_ports_sysfs i2c-nct6775
echo '24c02 0x50' > /sys/bus/i2c/devices/i2c-1/new_device       
