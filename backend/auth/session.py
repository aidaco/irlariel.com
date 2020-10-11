# Aidan Courtney 2020, see license for details.

from fastapi import request

import .crypt

SESSION_ID_HEADER = 'session-token'
TOKEN_HEADER = 'access-token'

def _user_loader(id_: int):
    # TODO docs
    # internal call back to user loader
    return None

def set_userloader(f: Callable):
    # TODO docs
    # ? set user loader
    _user_loader = f

class AuthLevel(str, Enum):
    """Stores level of authorization as an enum."""

    Basic = AuthLevel('basic', 0)
    Moderator = AuthLevel('mod', 1)
    Admin = AuthLevel('admin', 2)
    Developer = AuthLevel('dev', 3)

    def __init__(s: str = '', priority: int = 0):
        super().__init__(s)
        self.prio = priority

class AuthSession:
    """Implements session based authentication."""

    SESSION_LENGTH = 10800

    has_auth = False
    raw_auth = None
    session_key = None

    def __init__(request: request, *args, **kwargs):
        # TODO docs
        # ? constructor function
        super().__init__(*args, **kwargs)
        self.user = _user_loader(id_)

        self.user.session_key

    @staticmethod
    def authenticate(request):
        if self.has_auth:
            # TODO 200
            pass
        elif not self.can_auth:
            # TODO 401
            pass
        
        # ? Read headers
        token = request.headers.get(TOKEN_HEADER, None)

        if not token:
            # TODO 401
            pass

        # ? Handle authentication
        payload = crypto.decrypt()

        return auth_valid