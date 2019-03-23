"""
Arbitrary Data Reader
jl3560@rit.edu
9/25/18

Reads certain formatted data and places it into influx database

"""
from influxdb import InfluxDBClient

labls = ['time','gear','rpm','oilpres','speed','intakeairtemp','enginetemp','oiltemp','volt']
filename = 'telemetry-data.csv'

def main():
    
    #credentials
    host='localhost'
    port=8086
    #user = 'admin'
    #password = 'temp'
    dbname = 'Telemetry'

    print("initiating client")
    client = InfluxDBClient(host, port, dbname)
    # uncomment to create database, unnecessary when preexisting
    #print("creating database") 
    #client.create_database(dbname)
    with open(filename) as csv:
        time = 0.0
        for line in csv:
            vals = line.split(',')   # split line

            if vals[0] == 'wait': # keep track of time
                time += float(vals[1])
                #uncomment if time is wanted (extra 2 milliseconds per line)
                #client.write_points(genJson(labls[0], time), database=dbname)

            else:
                for i in range(8):  # write each measurement to its respective table
                    measurement = labls[i+1]
                    value = float(vals[i]) 
                    client.write_points(genJson(measurement, value), database=dbname)

# generate a proper json body for write_points
def genJson(measurement, val):
    json_body = [
            {
                "measurement": measurement,
                "fields": {
                    "value": val
                }
            }
        ]
    return json_body
        
if __name__ == '__main__': 
    main()
