from sqlalchemy.ext.asyncio import (
	AsyncSession,
	create_async_engine,
)

# from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


from main.config import settings



engine_psql_async_testing = create_async_engine(
	settings.PSQL_ASYNC_TESTING_URI,
	pool_pre_ping=True,
	# echo=True,
)


SessionPSQLAsyncTesting = sessionmaker(
	engine_psql_async_testing,
	expire_on_commit=False,
	class_=AsyncSession,
)
