"""
Arbitrary Data Reader
jl3560@rit.edu
9/25/18

Reads certain formatted data and places it into influx database

"""
from influxdb import InfluxDBClient

dictionary = {}
#make 2d list
labls = ['time','gear','nmot','poil','speed','tint','tmot','toil','ub']
for val in labls:
    dictionary[val] = []

def main():
    getData("telemetry-data.csv")
    print(str(dictionary['nmot']))
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
    time = 0.0
    file=open(filename, 'r')
    #add data to dictionary according to label
    for line in file:
        temp = line.split(",")
        if(temp[0] == "wait"):
            time += float(temp[1])
        else:
            dictionary[labls[0]].append(time)
            dictionary[labls[1]].append(float(temp[0]))
            dictionary[labls[2]].append(float(temp[1]))
            dictionary[labls[3]].append(float(temp[2]))
            dictionary[labls[4]].append(float(temp[3]))
            dictionary[labls[5]].append(float(temp[4]))
            dictionary[labls[6]].append(float(temp[5]))
            dictionary[labls[7]].append(float(temp[6]))
            dictionary[labls[8]].append(float(temp[7]))
        
if __name__ == '__main__': 
    main()