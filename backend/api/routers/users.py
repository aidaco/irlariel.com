# Aidan Courtney 2020, see incl. license for details.

from fastapi import APIRouter

import auth
from auth import AuthLevel

router = APIRouter()

# GET

@router.get('/')
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

@router.get('/me')
@auth.require(AuthLevel.Basic)
async def get_user_me():
    # TODO
    pass

@router.get('/{id_}')
@auth.require(AuthLevel.Moderator)
async def get_user(id_: str):
    # TODO
    pass

@router.get('/{ids}')
@auth.require(AuthLevel.Admin)
async def get_users(ids: list):
    # TODO
    # ? get a given list of users by id
    # ? optional query by fields? search? sort by?
    pass

# POST

@router.post('/')
async def new_user():
    # TODO
    pass

@router.delete('/me')
@auth.require
async def delete_self():
    # TODO
    pass

@router.post('/{id_}')
@auth.require(AuthLevel.Admin)
async def update_user(id_: str):
    # TODO
    pass

# DELETE

@router.delete('/{id_}')
@auth.require(AuthLevel.Admin)
async def delete_user(id_: str):
    # TODO
    pass