from datetime import datetime as dt

def calculate_age(bd):
    try:
        bd = dt.strptime(bd, '%Y/%m/%d')
    except:
        print('WRONG')
        return
    today = dt.today()
    if bd > today :
        print('WRONG')
        return
    age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
    print(age)

calculate_age(input())