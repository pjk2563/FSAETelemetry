"""
Arbitrary Data Maker
pjk2563@rit.edu
9/18/18

Generates random data and writes to a csv file
for testing telemetry frontend
"""
import random

def WriteData(fname, label, num):
    '''
    :param label: label to identify data with
    :param num: number of instances to write
    '''
    if label == 'gear':
        fname.write(label + ',' + str((num % 4) + 1) + '\n')
    
    else:
        for i in range(num):
            fname.write(label + ',' + str(random.uniform(1,50)) + '\n')

def main():
    iterLimit = 500
    labls = ['rpm', 'volt', 'gear', 'tmp', 'spd', 'gfs']
    with open("random.dat", 'a') as datfile:
        for i in range(iterLimit):
            for lab in labls:
                WriteData(datfile, lab, random.randint(1,10))


if __name__ == '__main__':
    main()
