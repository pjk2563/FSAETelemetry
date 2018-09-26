"""
Arbitrary Data Reader
jl3560@rit.edu
9/25/18

Reads certain formatted data and places it into influx database
"""

from influxdb import InfluxDBClient
'''
client = InfluxDBClient(host, port, user, password, dbname)

client.create_database(dbname)

 json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        }
    ]

client.write_points(json_body)
'''
dictionary = {}
#make 2d list
labls = ['rpm', 'volt', 'gear', 'tmp', 'spd', 'gfs']
for val in labls:
    dictionary[val] = []

def main():
    getData("random.dat")
    #print(dictionary['rpm'])

def getData(filename):
    file=open(filename, 'r')
    #add data to dictionary according to label
    for line in file:
        temp = line.split(",")
        if temp[0] in dictionary.keys():
            dictionary[temp[0]].append(float(temp[1]))
        else:
            dictionary[temp[0]] = float(temp[1])
    
main()