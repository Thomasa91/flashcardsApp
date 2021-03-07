from hashlib import sha256

# TODO  Maybe later try to use cryptography library, using key to hash password ?
# https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/

h = sha256()


def hash_password(password):

    h.update(bytes(password, "utf-8"))

    return h.hexdigest()
