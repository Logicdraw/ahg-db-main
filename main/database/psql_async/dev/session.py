from sqlalchemy.ext.asyncio import (
	AsyncSession,
	create_async_engine,
)

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


from main.config import settings



engine_psql_async_dev = create_async_engine(
	settings.PSQL_ASYNC_DEV_URI,
	pool_pre_ping=True,
	echo=True,
)



SessionPSQLAsyncDev = sessionmaker(
	engine_psql_async_dev,
	expire_on_commit=False,
	class_=AsyncSession,
)



