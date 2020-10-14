# Aidan Courtney 2020, see incl. license for details.

from enum import Enum
from typing import Callable
from auth.models import UserBase, AccessToken, AuthLevel
from pydantic import BaseModel
from fastapi import APIRouter, Request


class AuthSession(BaseModel):
    access_token: Optional[AccessToken] = None
    user: Optional[UserBase] = None
    is_authenticated: bool = False
    auth_level = AuthLevel.Basic

    def __init__(self, request: Request, authorization=Header(None)):
        secret_key = request.state.env["SECRET_KEY"]
        db = request.state.db

        access_token = AccessToken(token=authorization.split(" ")[1])
        data = access_token.verify(secret_key)
        if not (user_id := data.get("user_id")):
            return AuthSession(access_token=access)

        user = db.get_user(user_id)
        return AuthSession(
            access_token=access_token,
            user=user,
            is_authenticated=True,
            auth_level=user.auth_level,
        )


class Auth(AuthSession):
    @staticmethod
    def required(level: AuthLevel = AuthLevel.Basic):
        # TODO
        # ? wrap super __init__ to get AuthSession
        # ? and enforce given AuthLevel

        def wrapper(*args, **kwargs):
            authsession = self.__init__(*args, **kwargs)
            # TODO

        return wrapper
