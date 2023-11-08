import mysql.connector
import getpass
try:
    passw = getpass.getpass('please enter your root password ')
    print('connecting ')
except:
    print('Wrong password')
try: 
    cnx = mysql.connector.connect(user='root',
                              password=passw,
                              host='127.0.0.1',
                              database='test1')
    print("connected")
    curser = cnx.cursor()
    curser.execute("INSERT INTO peaple VALUES ('sana', 21, 'f')")
    cnx.commit()
    cnx.close()
except:
    print('Wrong password')
