"""
Arbitrary Data Reader
jl3560@rit.edu
9/25/18

Reads certain formatted data and places it into influx database

"""
from influxdb import InfluxDBClient

dictionary = {}
#make 2d list
labls = ['rpm', 'volt', 'gear', 'tmp', 'spd', 'gfs']
for val in labls:
    dictionary[val] = []

def main():
    getData("telemetry-data.csv")
    print(str(dictionary['rpm']))
    """
    host='192.168.43.1'
    port=3000
    user = 'admin'
    password = 'temp'
    dbname = 'FSAETelemetry'

    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.write_points([dictionary])"""

def getData(filename):
    file=open(filename, 'r')
    #add data to dictionary according to label
    for line in file:
        temp = line.split(",")
        if(temp[0] == "ECU_IDprim"):
            dictionary[labls[0]].append(float(temp[1]))
            dictionary[labls[1]].append(float(temp[2]))
            dictionary[labls[2]].append(float(temp[3]))
            dictionary[labls[3]].append(float(temp[4]))
            dictionary[labls[4]].append(float(temp[5]))
            dictionary[labls[5]].append(float(temp[6]))
        
if __name__ == '__main__': 
    main()