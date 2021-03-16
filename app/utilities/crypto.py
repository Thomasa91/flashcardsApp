from hashlib import sha256
from app import logger
# TODO  Maybe later try to use cryptography library, using key to hash password ?
# https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/

log = logger.getChild(__name__)

h = sha256()


def hash_password(password):
    log.debug("hashing password")
    h.update(bytes(password, "utf-8"))

    return h.hexdigest()
