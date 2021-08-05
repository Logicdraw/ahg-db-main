# ---
from main.database.base import *

# from main.database.base import Base


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from sqlalchemy.ext.asyncio import (
	AsyncConnection,
	AsyncSession,
)


from main.schemas import UserSchemaCreate

from main.config import settings

from main.crud import user_crud



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



async def create_first_superadmin_psql_async_db(
	engine_psql_async,
) -> None:
	# Create First Superadmin --

	email = settings.FIRST_SUPERADMIN_EMAIL
	password = settings.FIRST_SUPERADMIN_PASSWORD.get_secret_value()
	confirm_password = password
	name = settings.FIRST_SUPERADMIN_NAME
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	async with engine_psql_async.begin() as conn:
		async with AsyncSession(conn, expire_on_commit=False) as db:
			user = await user_crud.create(
				db=db,
				obj_in=user_in,
			)

	return None



async def create_first_admin_psql_async_db(
	engine_psql_async,
) -> None:
	# Create First Admin --

	email = settings.FIRST_ADMIN_EMAIL
	password = settings.FIRST_ADMIN_PASSWORD.get_secret_value()
	confirm_password = password
	name = settings.FIRST_ADMIN_NAME
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	async with engine_psql_async.begin() as conn:
		async with AsyncSession(conn, expire_on_commit=False) as db:
			user = await user_crud.create(
				db=db,
				obj_in=user_in,
			)

	return None



async def create_first_coach_psql_async_db(
	engine_psql_async,
) -> None:
	# Create First Coach --

	email = settings.FIRST_COACH_EMAIL
	password = settings.FIRST_COACH_PASSWORD.get_secret_value()
	confirm_password = password
	name = settings.FIRST_COACH_NAME
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	async with engine_psql_async.begin() as conn:
		async with AsyncSession(conn, expire_on_commit=False) as db:
			user = await user_crud.create(
				db=db,
				obj_in=user_in,
			)

	return None



async def create_first_guardian_psql_async_db(
	engine_psql_async,
) -> None:
	# Create First Guardian --

	email = settings.FIRST_GUARDIAN_EMAIL
	password = settings.FIRST_GUARDIAN_PASSWORD.get_secret_value()
	confirm_password = password
	name = settings.FIRST_GUARDIAN_NAME
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	async with engine_psql_async.begin() as conn:
		async with AsyncSession(conn, expire_on_commit=False) as db:
			user = await user_crud.create(
				db=db,
				obj_in=user_in,
			)

	return None




async def create_first_adult_rep_psql_async_db(
	engine_psql_async,
) -> None:
	# Create First Guardian --

	# if not ...

	email = settings.FIRST_ADULT_REP_EMAIL
	password = settings.FIRST_ADULT_REP_PASSWORD.get_secret_value()
	confirm_password = password
	name = settings.FIRST_ADULT_REP_NAME
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	async with engine_psql_async.begin() as conn:
		async with AsyncSession(conn, expire_on_commit=False) as db:
			user = await user_crud.create(
				db=db,
				obj_in=user_in,
			)

	return None



