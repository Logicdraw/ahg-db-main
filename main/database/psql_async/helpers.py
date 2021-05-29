# ---
from main.database import base

from main.database.base_class import Base


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)






async def init_psql_async_db(
	engine_psql_async,
) -> None:
	# Init DB --

	async with engine_psql_async.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)

	return None



async def drop_psql_async_db(
	engine_psql_async,
) -> None:
	# Drop DB --

	async with engine_psql_async.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)

	return None



async def reset_psql_async_db(
	engine_psql_async,
) -> None:
	# Reset DB --

	await drop_psql_async_db(engine_psql_async)
	await init_psql_async_db(engine_psql_async)

	return None




