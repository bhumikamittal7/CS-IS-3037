data = 'CAPTURETHEFLAG'
key = 'A'
encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
print(encrypted)
decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])
print(decrypted)