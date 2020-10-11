# Aidan Courtney 2020, see incl. license for details.

from fastapi import APIRouter

import auth
from auth import AuthLevel

router = APIRouter()



# GET

@router.get('/')
async def get_products():
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

@router.get('/{id_}')
async def get_product(id_: int):
    # TODO
    pass

@router.get('/{ids}')
async def get_products_by_id(ids: list):
    # TODO
    # ? get a given list of products by ids
    pass

# POST

@router.post('/')
@auth.require(AuthLevel.Moderator)
async def new_product():
    # TODO
    pass

@router.post('/{id_}')
@auth.require(AuthLevel.Moderator)
async def update_product(id_: int):
    # TODO
    pass

# DELETE

@router.delete('/{id_}')
@auth.require(AuthLevel.Moderator)
async def delete_product(id_):
    # TODO
    pass