from hashlib import sha256
from app.src.utilities.logger import logger
# TODO  Maybe later try to use cryptography library, using key to hash password ?
# https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/


def hash_password(password) ->str:
    h = sha256()
    logger.debug("Hashing password")
    h.update(bytes(password, "utf-8"))

    return h.hexdigest()

def check_password_hash(hashed_password, password) -> bool:

    return hash_password(password) == hashed_password
