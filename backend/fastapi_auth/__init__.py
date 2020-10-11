# Aidan Courtney 2020, see incl. license for details.

from enum import Enum
from typing import Callable
from auth.models import UserBase, SessionKey, AccessToken, AuthLevel
from fastapi import APIRouter, Request


def require_auth(level: AuthLevel):
    # TODO
    # ? decorator to require an AuthSession with specified AuthLevel
    pass

async def require_login(f: Callable):
    # TODO
    # ? decorator to require a valid AuthSession to access
    pass

class Authentication:
    async def __call__(self, request: Request, call_next: Callable):
        # TODO docs
        auth = AuthSession.from_request(request)
        request.state.auth = auth
        response = await call_next(request)
        return response

def _userloader(id_: str) -> UserBase:
    return None

def set_userloader(f: Callable):
    # TODO
    # ? User should call to set userloader
    _userloader = f

class AuthSession(pydantic.Model):
    access_token: Optional[AccessToken] = None
    user: Optional[UserBase] = None
    req_signature: Optional[RequestSignature] = None
    is_authenticated: bool = False
    auth_level = AuthLevel.Basic
    
    @staticmethod
    def from_request(request: Request):
        # TODO
        
        secret_key = request.state.env['SECRET_KEY']
        at_header = request.state.env['ACCESS_HEADER']
        rst_header = request.state.env['REQUEST_SIGNATURE_HEADER']

        atoken = request.headers.get(at_header, None)
        rstoken = request.headers.get(rs_header, None)

        if not at:
            return AuthSession()

        access = AccessToken.from_token(key, atoken)

        if not access.is_valid:
            return AuthSession(access_token=access)
        
        try:
            user = _userloader(access.payload['user_id'])
        except:
            return AuthSession(access_token=access)

        rsig = RequestSignature.from_token(user.session_key, rstoken)

        if not sig.is_valid:
            return AuthSession(access_token=access, user=user)
        
        return AuthSession(
            access_token=access, 
            user=user, 
            req_signature=rsig, 
            is_authenticated=True,
            auth_level=user.auth_level
        )