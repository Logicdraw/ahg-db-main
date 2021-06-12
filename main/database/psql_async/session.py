# Create PSQL ASYNC Session --


from sqlalchemy.ext.asyncio import (
	AsyncSession,
	create_async_engine,
)

# from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


from main.config import settings



echo_on = True

if settings.DEVELOPMENT:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_DEV_URI
elif settings.TESTING:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_TESTING_URI
elif settings.STAGING:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_DEV_URI
elif settings.PRODUCTION:
	SQLALCHEMY_URI = settings.PSQL_ASYNC_PROD_URI
	echo_on = False




engine_psql_async = create_async_engine(
	SQLALCHEMY_URI,
	pool_pre_ping=True,
	echo=echo_on,
)



SessionPSQLAsync = sessionmaker(
	engine_psql_async,
	expire_on_commit=False,
	class_=AsyncSession,
)




