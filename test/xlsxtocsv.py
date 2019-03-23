from openpyxl import load_workbook
import sys

def main():
    filename = sys.argv[1]
    nfilename = sys.argv[2]

    print("reading .xlsx file...")
    wb = load_workbook(filename)
    with open(nfilename, "w+") as csv:
        print("converting...")
        data = wb['Data']
        r = len(data['A'])
        lastprog = -1
        for i in range(2,r):
            prog = int((i / r) * 100)
            if prog != lastprog:
                print(str(prog) + "%", end = "\r")
                lastprog = prog
            csv.write(data["B" + str(i)].value.strip() + ","
            + data["C" + str(i)].value.strip() + ","
            + data["D" + str(i)].value.strip() + ","
            + data["E" + str(i)].value.strip() + ","
            + data["F" + str(i)].value.strip() + ","
            + data["G" + str(i)].value.strip() + ","
            + data["H" + str(i)].value.strip() + ","
            + data["I" + str(i)].value.strip() + "\n")

            time_stamp = float(data["A" + str(i+1)].value) - float(data["A" + str(i)].value)
            csv.write("wait," + str(time_stamp) + "\n")
if len(sys.argv) != 3:
    print('Usage: python3 xlsxtocsv.py <.xlsx file input> <.csv file output>')
else:
    main()
