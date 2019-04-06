"""
CAN Message Data Reader
pjk2563@rit.edu
4/6/2019

Sorts CAN data and places it into influx database

"""
from influxdb import InfluxDBClient
import serial

labls = [
    'time',
    'gear',
    'rpm',
    'oilpres',
    'speed',
    'intakeairtemp',
    'enginetemp',
    'oiltemp',
    'volt',
    'lftiretemp',
    'lrtiretemp',
    'rftiretemp',
    'rrtiretemp',
    'gaslevel'
]

serialdev = "/dev/ttyUSB0"
serialbaud = 115200

def dash1(msgData):
    rpm = int(vals[0] + vals[1], 16)
    oilt = int(vals[2], 16)
    watert = int(vals[3], 16)
    oilp = int(vals[4], 16)
    gear = int(vals[5], 16)
    batt = int(vals[6] + vals[7], 16)
    print(rpm + " RPM")
    print("Oil Temp: " + oilt + " C")
    print("Water Temp: " + watert + " C")
    print("Oil Pressure: " + oilp + " Pa")
    print(gear + " gear");
    print(batt + "V")

def dash2(msgData):
    pass

def lftiret(msgData):
    print("LF Tire Temp Can msg: " + msgData)

def lrtiret(msgData):
    print("LR Tire Temp Can msg: " + msgData)

canIdCaller = {
    '0x90': dash1,           # Dash 1
    '0xA0': dash2,           # Dash 2
    '0x100': lftiret,        # LF Tire Temp
    '0x110': lrtiret         # LR Tire Temp
}

def main():
        
    #credentials
    host='localhost'
    port=8086
    #user = 'admin'
    #password = 'temp'
    dbname = 'Telemetry'

    print("initiating database client")
    client = InfluxDBClient(host, port, dbname)

    print("initiating serial connection")
    with serial.Serial(serialdev, serialbaud) as ser:
        while True:
            msgId = ser.readline()
            msgData = ser.readline()
            if msgId in canIdCaller.keys():
                # if message is valid, interpret it's data
                if checkMessage(msgData):
                    canIdCaller[msgId](msgData)

def checkMessage(msgData):
    vals = msgData.split('\t')   # split line by tab
    checkValve = True
    # check if message is valid
    if len(vals) == 8:
        for i in vals:
            if len(vals[i]) != 2: 
               checkValve = False 
    return checkValve

"""
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
"""

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
