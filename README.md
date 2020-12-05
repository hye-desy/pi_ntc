# pi_ntc

Read NTC thermistors using raspberry+MCP3008


# measure_gpio.py

use arbitrary GPIO to select chip, need to add 'dtoverlay=spi0-hw-cs' in "/boot/config.txt"


# measure_sc.py

use GPIO8,7 (spi0.CE0/1) or spi1 to select chip, to use spi1, need to add 'dtoverlay=spi1-3cs' in "/boot/config.txt"
