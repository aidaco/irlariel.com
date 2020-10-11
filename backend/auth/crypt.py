# Aidan Courtney 2020, see incl. license for details.

from random import SystemRandom
import base64
import os
from typing import Callable
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def b64urldecoder(**fields_to_dec):
    def _b64decoder(f: Callable):
        # TODO
        # ? decorator to url-safe base64 decode fields passed as
        # ? {..., {field_name:True},...}
        params = inspect.signature(f, follow_wrapped=True).parameters

        def wrapper(*args, **kwargs):
            for i, p in enumerate(params):
                if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD):
                    if p.name in kwargs:
                        continue
                    args[i] = base64.urlsafe_b64decode(str(args[i]))
                    continue
                kwargs[p.name] = base64.urlsafe_b64decode(str(kwargs[p.name]))
            return f(*args, **kwargs)


def gen_session_key(secret: bytes):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    return base64.urlsafe_b64encode(kdf.derive(secret))
    

class SessionKey(bytes):
    # TODO docs

    def __init__(self, key: bytes = None, secret: bytes = None):
        # TODO docs
        self.key = key

        if secret:
            self.new_key(secret)
    
    def new_key(self, secret: bytes):
        # TODO docs
        if self.key:
            raise Exception('SessionKey Already set.')    
        
        self.key = gen_session_key(secret)
    
    def decrypt(self, token: bytes):
        # TODO docs
        return decrypt(self.key, token)
        

class SessionAccessToken(bytes):
    # TODO docs

    def __init__(self, token: bytes = None):
        # TODO docs
        self.__token__ = token
    
    @property
    def token(self):
        if self.__token__:
            return self.__token__


    @property.get()
    def new_token(self, user):
        # TODO docs
        # ? take data from user to produce a SessionIDToken

        if self.key:
            raise Exception("SessionIDToken has already been created")

        payload = {
            'username':'aidan',
            'ttl':100
        }

        self.payload_bytes = bytes(str(payload))

        return encrypt(self.key, self.payload_bytes)
    
    @b64urldecoder(payload=True)
    def validate(self, payload: bytes):
        # TODO docs
        # ? validate the payload
        # ? return False, {Exception}
        # ? or True, data
        try:
            data = decrypt(self.key, payload)
        except Exception as e:
            return False, e
        return True, data

def encrypt(key: bytes, payload: bytes):
    f = Fernet(key)
    return f.encrypt(payload)

def decrypt(key: bytes, token: bytes):
    f = Fernet(key)
    return f.decrypt(token)