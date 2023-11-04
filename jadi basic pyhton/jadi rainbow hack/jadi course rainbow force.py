import hashlib
import csv 
from os.path import dirname, join

#this is a function that returns the sha 256 hash of inputed data
def sha256(data):
    m = hashlib.sha256()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

#this makes a dict containing all numbers from 0000 to 9999 and their sha256 hashes
dic = {}
for i in range(10000):
    i = '{0:04}'.format(i)
    dic.update({sha256(i):i})

#this opens a csv file containing usernames and hashed password
filename = 'passwords.csv'
file = open(join(dirname(__file__), "./{}".format(filename)))
#file = open('C:\\Users\sam\Desktop\proj\passwords.csv')

#print(type (file))
csvreader = csv.reader(file)
namehash = []
for row in csvreader:
    namehash.append(row)

#this brute force and finds all the password from their hashes, and then print the username and the password in a row
for i in range(0, len(namehash)):
    print("{}-{}".format(namehash[i][0], dic[namehash[i][1]]))