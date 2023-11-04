import csv
with open('c:\Users\sam\Desktop\jadi csv test\test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)