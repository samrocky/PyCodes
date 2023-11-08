import mysql.connector
import getpass
import re 

def emailcheck(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    if re.match(regex, email):
        return True
    else:
        return False

def connect(p = ''):
    while True:
        dbname = input("Please Enter Your Database Name: ")
        passw = getpass.getpass('Please Enter Your root Password: ') if p == '' else p
        #print('Connecting ')
    
        try:
            global cnx
            global curser
            cnx = mysql.connector.connect(user='root',
                                        password=passw,
                                        host='127.0.0.1',
                                        database=dbname)
        
            curser = cnx.cursor()
            print("Connected")
            break

        except:
            print('Wrong password or database name')
            continue

def write():
    while True:
        table = input("Please Entre Your Table Name: ")
        while True:
            username = input("Please Enter a Username (close for closing): ")
            if username != 'close':
                if emailcheck(username):
                    pass
                else:
                    print("Wrong Format, Use the Following Format: expression@string.string")
                    continue
                password = input("Please Enter password: ")
                try:   
                    curser.execute("INSERT INTO %s VALUES ('%s', '%s')" % (table, username, password))
                    cnx.commit()
                except:
                    print("Table '%s' doesn't exist" % (table))
                    break
            else:
                cnx.close()
                print("closing")
                exit()

connect()
write()