from starlette.config import Config

config = Config('.env')

if __name__ != '__main__':
    from .common import *
    from .db import *
