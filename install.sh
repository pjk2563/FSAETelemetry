echo This is the install script that will handle the installation of the telemetery system on reciever pi
su -
apt-get update && apt-get full-upgrade -y
apt-get install curl -y
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
apt-get update && apt-get upgrade -y
apt-get install influxdb -y
service influxdb start
#Will add the grafana install instructions when I have my hands on a pi
