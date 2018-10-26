# [FSAETelemetry]
Remote Telemetry Project

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
