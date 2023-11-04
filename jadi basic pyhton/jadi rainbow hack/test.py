import hashlib
def sha256(data):
        m = hashlib.sha256()
        m.update(data.encode('utf-8'))
        return m.hexdigest()

lst = ['1234', '1230', '1111', '0000', '1212', '5555', '4464', '5050']
for password in lst:
        print(sha256(password))