import os
import mysql.connector
import base64
from Crypto.Cipher import AES
import json

cnx = mysql.connector.connect(user='root', password='***************',
                              host='192.168.1.21',
                              database='employees')

mycursor = cnx.cursor()

files = os.listdir("C://keyiv")
os.chdir("C://keyiv")
filedict = {}

for file in files:
    with open(file, "r") as f:
        text = f.read()
        filedict[file.rstrip(".txt")] = text.split()

def decrypt(encrypt, file_name):
    key = filedict.get(file_name)[0]
    iv = filedict.get(file_name)[1]
    iv = base64.b64decode(iv)
    key = base64.b64decode(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(base64.b64decode(encrypt))
    return result.decode()

mycursor.execute("SELECT * FROM decryptiontable")
results = mycursor.fetchall()
json_data={}
for result in results:
    decrypted = decrypt(result[1], result[2])
    json_data[result[1]] = decrypted.rstrip()

os.chdir("C://Users/foras/PycharmProjects/Python-Projects")

with open ("test.json", "r+") as f:
    f.truncate(0)

with open("test.json", "w") as f:
    json.dump(json_data, f, indent=4, separators=(", ", ": "), sort_keys=True, default=str)

cnx.close()