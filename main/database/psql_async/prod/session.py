from sqlalchemy.ext.asyncio import (
	AsyncSession,
	create_async_engine,
)

# from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


from main.config import settings



engine_psql_async_prod = create_async_engine(
	settings.PSQL_ASYNC_PROD_URI,
	pool_pre_ping=True,
	echo=False,
)



SessionPSQLAsyncProd = sessionmaker(
	engine_psql_async_prod,
	expire_on_commit=False,
	class_=AsyncSession,
)


