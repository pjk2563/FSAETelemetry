"""
CAN Message Data Reader
pjk2563@rit.edu
4/6/2019

Sorts CAN data and places it into influx database

"""
from influxdb import InfluxDBClient
import serial

# unused
labls = [
    'speed',
    'intakeairtemp',
    'lftiretemp',
    'lrtiretemp',
    'rftiretemp',
    'rrtiretemp',
    'gaslevel'
]

serialdev = "/dev/ttyUSB0"
serialbaud = 115200

def dash1(msgData):
#     print("new 0x90 message")
    vals = msgData.split("\t")
    rpm = int(vals[0] + vals[1], 16)
    oilt = int(vals[2], 16)
    watert = int(vals[3], 16)
    oilp = int(vals[4], 16)
    gear = int(vals[5], 16)
    batt = int(vals[6] + vals[7], 16)
    return {
        'rpm': rpm,
        'oiltemp': oilt,
        'enginetemp': watert,
        'oilpres': oilp,
        'gear': gear,
        'volt': batt
    }

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
            msgId = ser.readline().strip().decode("UTF-8")
            msgData = ser.readline().strip().decode("UTF-8")
            if msgId in canIdCaller.keys():
                # if message is valid, interpret it's data
                if checkMessage(msgData):
                    vals = canIdCaller[msgId](msgData)
                    # print("writing measurements")
                    for measurement in vals.keys():
                        client.write_points(
                            genJson(measurement, 
                                float(vals[measurement])), 
                            database=dbname)

def checkMessage(msgData):
    vals = msgData.split('\t')   # split line by tab
    checkValve = True
    # check if message is valid
    if len(vals) != 8:
        checkValve = False
    else:
        for s in vals:
            if len(s) > 2: 
               checkValve = False 
    return checkValve

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
