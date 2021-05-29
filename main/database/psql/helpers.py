# ---
from main.database import base

from main.database.base_class import Base


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# from main.psql.session import engine_psql
# Base




def init_psql_db(
	engine_psql,
) -> None:
	# Init psql db --

	Base.metadata.create_all(bind=engine_psql)


def drop_psql_db(
	engine_psql,
) -> None:
	# Drop psql db --

	Base.metadata.drop_all(bind=engine_psql)



def reset_psql_db(
	engine_psql,
) -> None:
	# Reset psql db --

	drop_psql_db(engine_psql)
	init_psql_db(engine_psql)





