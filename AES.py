import base64
from Crypto.Cipher import AES

str ="kristi          "
key64 = b"2HVSxAQ4IaEu4MYegwdGAw=="
iv64 = b"d0sVFLWjavRlsTIONoucsg=="

iv = base64.b64decode(iv64)
key = base64.b64decode(key64)
cipher = AES.new(key, AES.MODE_CBC, iv)
encoded = base64.b64encode(cipher.encrypt(str.encode()))
print(encoded)
cipher2= AES.new(key, AES.MODE_CBC, iv)

print(cipher2.decrypt(base64.b64decode(encoded)))