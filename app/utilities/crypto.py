from hashlib import sha256

#TODO how to name that folder 
#TODO  Maybe later try to use cryptography library, using key to hash password ?
# https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/

h = sha256()

def hash_password(password):

    h.update(password)

    return h.hexdigest().encode('utf-8')