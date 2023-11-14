#imports:
import mysql.connector
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import datetime
import pandas as pd
import numpy as np

#functions:
def connect():
    dbname = 'cars'
    username = 'root'
    passw = '1230'
    try:
        global cnx
        global curser
        cnx = mysql.connector.connect(user=username,
                                        password=passw,
                                        host='127.0.0.1',
                                        database=dbname)
        curser = cnx.cursor()
        print('Connected')
    except:
        print('Wrong password, username or database name')
        exit()
def read():
    x = []
    y = []
    query  = "SELECT DISTINCT * FROM cars;"
    curser.execute(query)
    for i in curser:
        xs = list(i[0:6])
        xs = [str(i) for i in xs]
        # Change the Year column to the years of usage
        xs[3] = str(datetime.date.today().year - int(xs[3]))
        xs[3] = pd.to_numeric(xs[3])
        xs[-1] = pd.to_numeric(xs[-1])
        xs = [xs[0], xs[1], xs[3], xs[-1]]
        x.append(xs)
        y.append((i[-1]))
    x = pd.get_dummies(x)
    return x, y, xs


connect()
x, y = read()

#this part of the project is not complited yet because of lack of my knowledge about Machine Learning
'''
clf = LinearRegression()
clf = clf.fit(x, y)
'''