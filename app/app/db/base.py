import databases
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import config


def get_db() -> databases.Database:
    database_url = config.DATABASE_URL
    options = {
        "min_size": config.DB_MIN_SIZE,
        "max_size": config.DB_MAX_SIZE,
        "force_rollback": config.DB_FORCE_ROLL_BACK,
    }

    return databases.Database(database_url, **options)


database = get_db()
Base = declarative_base()
metadata = Base.metadata
