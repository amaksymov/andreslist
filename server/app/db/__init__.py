import logging

import databases
import sqlalchemy

from app.settings import DATABASE_URL

log = logging.getLogger(__name__)

db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


async def startup_db():
    try:
        await db.connect()
        log.info("Database connected.")
    except Exception as e:
        log.error(e)


async def shutdown_db():
    await db.disconnect()
