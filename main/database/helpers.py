from sqlalchemy.orm import Session

from main.config import get_settings
settings = get_settings()


from main.database import base  # noqa: F401


from main.database.base_class import Base



import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




# make sure all SQL Alchemy models are imported (app.database.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28



def init_db(
	db: Session,
	engine,
) -> None:
	# Tables should be created with Alembic migrations
	# But if you don't want to use migrations, create
	# the tables un-commenting the next line
	# Base.metadata.create_all(bind=engine)

	Base.metadata.create_all(bind=engine)

	return None



def reset_db(
	db: Session,
	engine,
) -> None:	
	# Reset DB

	drop_db(db=db, engine=engine)
	init_db(db=db, engine=engine)

	return None



def drop_db(
	db: Session,
	engine,
) -> None:
	# Drop DB

	Base.metadata.drop_all(bind=engine)

	return None


