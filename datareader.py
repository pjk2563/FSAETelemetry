"""
Arbitrary Data Reader
jl3560@rit.edu
9/25/18

Reads certain formatted data and places it into influx database
"""
import argparse
from influxdb import InfluxDBClient

dictionary = {}
#make 2d list
labls = ['rpm', 'volt', 'gear', 'tmp', 'spd', 'gfs']
for val in labls:
    dictionary[val] = []

def main(host='192.168.43.1', port=3000):
    getData("random.dat")
    #print(dictionary['rpm'])
    user = 'admin'
    password = 'temp'
    dbname = 'FSAETelemetry'

    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.write_points([dictionary])

def getData(filename):
    file=open(filename, 'r')
    #add data to dictionary according to label
    for line in file:
        temp = line.split(",")
        if temp[0] in dictionary.keys():
            dictionary[temp[0]].append(float(temp[1]))
        else:
            dictionary[temp[0]] = float(temp[1])

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False, default='192.168.43.1', help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=3000, help='port of InfluxDB http API')
    return parser.parse_args()

if __name__ == '__main__': 
    args = parse_args()
    main(host=args.host, port=args.port)