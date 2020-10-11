# Aidan Courtney 2020, see incl. license.

DEFAULT_PAGE_LENGTH = 100

class DBInterface:
    def __init__(self, path):
        # TODO
        # ? connect to database, store as instance variable

    ## Users

    async def get_user(self, id_: str):
        # TODO
        pass

    async def get_users(self, ids: list):
        # TODO
        pass

    async def search_users(self, query: dict = None, limit: int = DEFAULT_PAGE_LENGTH, sort_by: str = None, order_by: str = None):
        # TODO
        pass

    async def update_user(self, **fields):
        # TODO
        # ? updates user[k] = v for k, v in fields
        pass

    async def delete_user(self, id_: str):
        # TODO
        pass


    ##Products

    async def get_product(self, id_: str):
        # TODO
        pass

    async def get_products(self, ids: list):
        # TODO
        pass

    async def search_products(self, query: tuple = None, limit: int = DEFAULT_PAGE_LENGTH, sort_by: str = None, order_by: str = None):
        # TODO
        pass

    async def update_product(self, id_: str, **fields):
        # TODO
        # ? updates product[k] = v for k, v in fields
        pass

    async def delete_product(self, id_: str):
        # TODO
        pass