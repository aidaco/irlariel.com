# Aidan Courtney 2020, see incl. license for details.

from random import SystemRandom
import base64
import os
from typing import Callable
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def gen_key(secret: bytes):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    return base64.urlsafe_b64encode(kdf.derive(secret))

def encrypt(key: bytes, payload: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(payload)

def decrypt(key: bytes, token: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(token)