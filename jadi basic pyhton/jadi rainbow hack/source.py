import hashlib
import csv
from os.path import dirname, join

def hash_password_hack(input_file_name, output_file_name):
    def sha256(data):
        m = hashlib.sha256()
        m.update(data.encode('utf-8'))
        return m.hexdigest()

    dic = {}
    for i in range(10000):
        i = '{0:04}'.format(i)
        dic.update({sha256(i):i})

    filename = input_file_name
    filein = open(join(dirname(__file__), "./{}".format(filename)))

    csvreader = csv.reader(filein)
    namehash = []
    for row in csvreader:
        namehash.append(row)
    fileout = open(join(dirname(__file__), "./{}".format(output_file_name)), 'w')
    for i in range(0, len(namehash)):
        a = "{},{}\n".format((namehash[i][0]).strip(), dic[(namehash[i][1]).strip()])
        fileout.write(a)
        print(a.strip())
    fileout.close()