from typing import Callable
from inspect import signature, Signature, Parameter

def typeswitch(**mapping: Callable):
    def _decorator(f: Callable):
        # TODO
        # ? decorator to typecast paramss passed as
        # ? {..., <param_name>:<constructor-like>,...}
        def wrapper(*args, **kwargs):
            __errors__ = []
            arguments = signature(f).bind(*args, **kwargs).arguments
                
            for param, func in mapping:
                    arguments[param] = func(args[param_name])
            return f(*arguments.args, **arguments.kwargs)
