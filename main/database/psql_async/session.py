# Create PSQL ASYNC Session--


from sqlalchemy.ext.asyncio import (
	AsyncSession,
	create_async_engine,
)

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


from main.config import settings



if settings.DEVELOPMENT or settings.STAGING:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_DEV_URI
elif settings.TESTING:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_TESTING_URI
elif settings.PRODUCTION:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_PROD_URI




engine_psql_async = create_async_engine(
	SQLALCHEMY_URI,
	pool_pre_ping=True,
	echo=True,
)



SessionPSQLAsync = sessionmaker(
	engine_psql_async,
	expire_on_commit=False,
	class_=AsyncSession,
)


