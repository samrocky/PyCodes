import mysql.connector
import getpass

def connect(p = None):
    passw = getpass.getpass('please enter your root password ') if p == None else p
    print('connecting ')

    try:
        global cnx
        global curser
        cnx = mysql.connector.connect(user='root',
                                      password=passw,
                                      host='127.0.0.1',
                                      database='test1')
        
        curser = cnx.cursor()
        print("connected")

    except:
        print('Wrong password')
        exit()

def write():
    while True:
        in_list = input('please enter values name age sex ')

        if in_list != 'close':
            in_list = in_list.split()
            
            for i in range(len(in_list)):
                try:
                    in_list[i] = int(in_list[i])
                except:
                    pass
            
            name = in_list[0]
            age = in_list[1]
            sex = in_list[2]
            curser.execute("INSERT INTO peaple VALUES ('%s', %i, '%s')" % (name, age, sex))
            cnx.commit()

        else:
            cnx.close()
            exit()

def read():
    pass

def mysqlscript():
    pass

connect()
write()
