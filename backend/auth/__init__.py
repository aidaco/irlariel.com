# Aidan Courtney 2020, see incl. license for details.

from enum import Enum
from typing import Callable

from .session import AuthLevel, AuthSession

from fastapi import APIRouter, request


router = APIRouter()


async def auth(f: Callable):
    # TODO
    # ? decorator
    # ? attempts to create an AuthSession and attach it to the request
    # ? does no validation, may include request artifacts for inspection
    pass

async def require(level: AuthLevel):
    f = auth(f)
    # TODO
    # ? decorates a function to require the given AuthLevel
    pass

async def require(f: Callable):
    # TODO
    # ? require valid AuthSession to access
    # ? utility equivalent to self.require(AuthLevel.BASIC)
    return require(AuthLevel.Basic)(f)