import asyncio

import pytest


from typing import (
	Dict,
	Generator,
	Any,
)

# from httpx import AsyncClient

from sqlalchemy.ext.asyncio import (
	AsyncConnection,
	AsyncSession,
)


from main.config import settings


from main.database.psql_async.testing.session import (
	engine_psql_async_testing,
)



@pytest.fixture()
async def connection():
	async with engine_psql_async_testing.begin() as conn:
		yield conn
		await conn.rollback() # Resets db.


@pytest.fixture()
async def db(connection: AsyncConnection):
	async with AsyncSession(connection, expire_on_commit=False) as _db:
		yield _db



@pytest.fixture(scope='session', autouse=True)
def event_loop():
	# Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154 --
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()







