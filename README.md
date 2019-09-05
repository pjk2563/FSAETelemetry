# [FSAETelemetry]
Project to remotely monitor telemetry of the car

# [Overview]
This project consists of 3 parts: an arduino with a radio, a raspberry pi with a radio, and a computer to view the data.

## [High level design]
The arduino with the radio is attached to the harness (wiring) of the car. This is how it will receive power, as well as how it will communicate over CAN (the communication protocol of the car). The arduino will read CAN using a CAN shield on the arduino. It will then send that information to an Xbee, which is a tiny radio wired to the arduino. The xbee then send information over radio to the receiving Xbee attached to the rapsberry pi. The raspberry pi then processes the data, and creates a local wifi network that someone can connect to and view live data. 

## [The Pi]
The raspberry pi reads in data from the xbee. This is done by reading some of the io pins on the pi. The datareader.py script is the script that will read the io. When it reads the io it receives a CAN message that it needs to decode. It looks at the CAN message and picks our the info needed. For example, if it is known that oil pressure is the 5th byte in a CAN message, this script will then parse the 5th bit as the oil pressure. This script then stores that information in a database call InfluxDB (link below). Then, a software called Grafana will read from this database to display a webpage

## [Getting started]
To set up the telemetry system, simply load either can_passthru.ino or serial_spoof.ino. can_passthru is the code to be used if it is running on the car, and serial_spoof is to be used for testing. Then all that is needed is to run the code on the arduino. Then, the pi must be plugged in and connected to the xbee. The pi should automatically start the webserver and wifi network to connect to. Then connect to the wifi network. Go into your browser and go to either fsae.telemetry:XXXX or the default gateway::XXXX. XXXX represents the port number, which can be found in the graphana config file.

## [Changing things]
To change what data is displayed you must ssh into the pi and edit datareader.py, graphana, and InfluxDB. For datareader, you need to change it to parse the proper info. For example, now it is parsing stuff like oil temperature. To parse current, you would need to know what byte in the can message represents current. Then you need to edit InfluxDB to store that data in a table, and graphana to graph it.

# [Raspberry Pi]
OS: Arch Linux Arm

Hostname: Telebot

User: ritfsae

Package manager: pacman

https://wiki.archlinux.org/index.php/pacman

# [Grafana]
directory: /home/ritfsae/grafana/

config: /etc/grafana.ini

logs: /home/ritfsae/grafana/data/log

enabled

# [InfluxDB]
config: /etc/influxdb/influxdb.conf

enabled

# [Python]
Python3 installed

python-influxdb client installed for python-database interaction

# [Internet Access]
Insert usb wireless card

use 'ip a' to determine interface label (most likely wlan1)

wpa_supplicant -i [interface] -B -c rit-conn.conf

dhcpcd [interface]

# [Automatic AP]
hostapd, for access point management. Config is at /etc/hostapd/hostapd.conf

dnsmasq, for dns and dhcp leasing. Config is at /etc/dnsmasq.conf

systemd-networkd, for persistent static ip. /etc/systemd/network/wlan0.network sets static ip on reboot for wlan0 interface. 


To set AP on boot:

systemctl enable hostapd

systemctl enable dnsmasq

/etc/systemd/network/wlan0.network {exists}

To disable AP on boot: 

WARNING: Without a dhcp server to connect the pi to, this will make the pi unnaccessible

systemctl disable hostapd

systemctl disable dnsmasq

mv /etc/systemd/network/wlan0.network /path/to/somewhere/else
