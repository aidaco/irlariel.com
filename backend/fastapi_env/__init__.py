# Aidan Courtney 2020, see incl. license for details.

from fastapi import Request

class Env(dict):
    @staticmethod
    def from_object(path):
        # TODO docs
        obj = __import__(path)
        conf = {str(k):str(v) for k,v in dir(obj)}
        return Env(**conf)

class Config:
    def __init__(self, path: str):
        # TODO docs
        self.env = Env.from_object(path)
    
    async def __call__(self, request: Request, call_next):
        request.state.env = self.env
        response = await call_next(request)
        return response