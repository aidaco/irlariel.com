# Aidan Courtney 2020, see incl. license for details.

from fastapi import APIRouter

import auth
from auth import AuthLevel

from . import BASE, router


RESOURCE = 'users'

BASEURL = f"{BASE}/{RESOURCE}"

# GET

@router.get(BASEURL)
@auth.require(AuthLevel.Admin)
async def get_users():
    # TODO
    # ? get all products
    # ? query param 'search': str = None,
    # ?     search field
    # ? query param 'query': str = None,
    # ?     value for above search field
    # ? query param 'limit': int = 100,
    # ?     limits num returned
    # ? query param 'sort': str = 'date,
    # ?     what to sort by
    # ? query param 'sort_order': str = 'desc'
    # ?     sort order
    pass

login = auth.login(BASEURL + '/login')
logout = auth.login(BASEURL + '/logout')

@router.get(BASEURL + '/me')
@auth.require(AuthLevel.Basic)
async def get_user_me():
    # TODO
    pass

@router.get(BASEURL + '/{id_}')
@auth.require(AuthLevel.Moderator)
async def get_user(id_: str):
    # TODO
    pass

@router.get(BASEURL + '/{ids}')
@auth.require(AuthLevel.Admin)
async def get_users(ids: list):
    # TODO
    # ? get a given list of users by id
    # ? optional query by fields? search? sort by?
    pass

# POST

@router.post(BASEURL)
async def new_user():
    # TODO
    pass

@router.delete(BASEURL + '/me')
@auth.require
async def delete_self():
    # TODO
    pass

@router.post(BASEURL + '/{id_}')
@auth.require(AuthLevel.Admin)
async def update_user(id_: str):
    # TODO
    pass

# DELETE

@router.delete(BASEURL + '/{id_}')
@auth.require(AuthLevel.Admin)
async def delete_user(id_: str):
    # TODO
    pass