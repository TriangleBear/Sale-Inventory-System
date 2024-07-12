from hashlib import sha256


print(sha256("Password!123".encode('utf-8')).hexdigest())