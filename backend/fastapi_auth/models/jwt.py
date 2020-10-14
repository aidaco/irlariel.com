# Aidan Courtney 2020, see incl. license for details.

import json
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel
from fastapi import Header

from fastapi_auth import crypto


class AccessToken(BaseModel):
    token: bytes
    alg: Optional[str] = 'HS256'
    data: Optional[dict] = None


    def verify(self, key: str):
        try:
            data = jwt.decode(token.token, key, algorithms=[token.alg])
            if data.get('exp') < datetime.now():
                return False
        except:
            return False
        return data


    @staticmethod
    def make(key: str, data: dict, dur: timedelta, alg: str = 'HS256'):
        # TODO docs
        # ? Produce an AccessToken

        data.update({'exp': datetime.now()+dur})
        token = jwt.encode(data), key, algorithm=alg)

        return AccessToken(token=token, alg=ALGORITHM, data=data)