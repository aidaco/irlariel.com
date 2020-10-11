# Aidan Courtney 2020, see incl. license for details.

from datetime import datetime, timedelta
import json
import pydantic
from fastapi import Request
from auth import crypto

class AuthLevel(str, Enum):
    """Stores level of authorization as an enum."""

    Basic = AuthLevel('basic', 0)
    Moderator = AuthLevel('moderator', 1)
    Admin = AuthLevel('admin', 2)
    Developer = AuthLevel('developer', 3)

    def __init__(s: str = '', priority: int = 0):
        super().__init__(s)
        self.prio = priority

class SessionKey(pydantic.BaseModel):
    __key__: bytes

    def encrypt(self, payload: bytes) -> bytes:
        # TODO docs
        return crypto.encrypt(self.__key__, payload)

    def decrypt(self, token: bytes) -> bytes:
        # TODO docs
        return crypto.decrypt(self.__key__, token)
    
    @staticmethod
    def from_secret(secret: bytes) -> SessionKey:
        return SessionKey(__key__=crypto.gen_key(secret))
    
    @staticmethod
    def from_existing(key: bytes) -> SessionKey:
        return SessionKey(__key__=key)

class UserBase(pydantic.BaseModel):
    id: Optional[str] = None
    password_hash: str
    auth_level = AuthLevel.Basic
    session_key: Optional[SessionKey] = None
    session_len: timedelta

class AccessToken(pydantic.BaseModel):
    payload: dict
    __token__: bytes
    is_valid = False
    
    @staticmethod
    def from_user(key: bytes, user: UserBase) -> AccessToken:
        # TODO docs
        # ? take data from user to produce an AccessToken

        payload = {
            'user_id': user.id,
            'auth': user.auth_level,
            'exp': datetime.now()+user.session_len
        }

        token = crypto.encrypt(key, json.dumps(payload).encode('utf-8'))

        return AccessToken(payload=payload, __token__=token, is_valid=True)
    
    @staticmethod
    def from_token(key: bytes, token: bytes) -> AccessToken:
        # TODO docs
        try:
            payload = json.loads(crypto.decrypt(key, token))
            return AccessToken(payload=payload, __token__=token, is_valid=True)
        else:
            return AccessToken(__token__=token)

class RequestSignature(pydantic.BaseModel):
    __token__: bytes
    payload: Optional[str] = None
    is_valid = False

    def authenticate(self, request: Request) -> bool:
        # TODO
        return False

    @staticmethod
    def from_token(key: SessionKey, token: bytes) -> RequestSignature:
        # TODO docs
        try:
            payload = key.decrypt(token)
            return RequestSignature(__token__=token, payload=payload, is_valid=True)
        except:
            return RequestSignature(__token__=token)