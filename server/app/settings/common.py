from . import config

API_V1_STR = config("API_V1_STR", cast=str, default="/api/v1")
SECRET_KEY = config("SECRET_KEY", cast=str, default="CHANGE_ME")
DEBUG = config("DEBUG", cast=bool, default=False)
