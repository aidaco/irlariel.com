# Aidan Courtney 2020, see incl. license for details.

from . import router, require

def login(path: str):
    @router.post(path)
    async def _login():
        # TODO
        # ? attempts to log in to an AuthSession
        pass
    return _login

def logout(path: str):
    @router.get(path)
    @require
    async def _logout(f: Callable):
        f = auth(f)
        # TODO
        # ? decorates a function to destroy the current AuthSession
        pass
    return _logout