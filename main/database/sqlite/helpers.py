# --
from main.database import base

from main.database.base_class import Base


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




def init_sqlite_db(
	engine_sqlite,
) -> None:
	# init SQLite --

	Base.metadata.create_all(bind=engine_sqlite)



def drop_sqlite_db(
	engine_sqlite,
) -> None:
	# drop SQLite --

	Base.metadata.drop_all(bind=engine_sqlite)


def reset_sqlite_db(
	engine_sqlite,
) -> None:
	# reset SQLite

	drop_sqlite_db(engine_sqlite)
	init_sqlite_db(engine_sqlite)
