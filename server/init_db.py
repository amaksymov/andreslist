async def init_db():
    """ Only for test """
    from app import db
    from app import users
    from app import get_password_hash

    await db.connect()
    await db.execute(users.insert(), {
        "username": "admin",
        "first_name": "John",
        "last_name": "Doe",
        "email": "echoes@ex.ua",
        "password_hash": get_password_hash("admin"),
    })


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
