from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.meta.gs import (
	gs_meta_crud,
)

from main.schemas.meta.gs import (
	GSMetaSchemaCreate,
	GSMetaSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await gs_meta_crud.create(
		db=db,
		obj_in=gs_meta_in,
	)

	assert gs_meta.access_token_encoded == access_token_encoded



@pytest.mark.asyncio
async def test_create_sync_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await db.run_sync(
		gs_meta_crud.create_sync,
		obj_in=gs_meta_in,
	)

	assert gs_meta.access_token_encoded == access_token_encoded



@pytest.mark.asyncio
async def test_get_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await gs_meta_crud.create(
		db=db,
		obj_in=gs_meta_in,
	)

	gs_meta_2 = await gs_meta_crud.get(
		db=db,
		id=gs_meta.id,
	)

	assert gs_meta_2
	assert jsonable_encoder(gs_meta_2) == jsonable_encoder(gs_meta)



@pytest.mark.asyncio
async def test_get_sync_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await db.run_sync(
		gs_meta_crud.create_sync,
		obj_in=gs_meta_in,
	)

	gs_meta_2 = await db.run_sync(
		gs_meta_crud.get_sync,
		id=gs_meta.id,
	)

	assert gs_meta_2
	assert jsonable_encoder(gs_meta_2) == jsonable_encoder(gs_meta)



@pytest.mark.asyncio
async def test_update_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await gs_meta_crud.create(
		db=db,
		obj_in=gs_meta_in,
	)

	new_access_token_encoded = random_lower_string()

	gs_meta_in_update = GSMetaSchemaUpdate(
		access_token_encoded=new_access_token_encoded,
	)

	gs_meta_2 = await gs_meta_crud.update(
		db=db,
		db_obj=gs_meta,
		obj_in=gs_meta_in_update,
	)

	assert gs_meta_2
	assert gs_meta_2.access_token_encoded
	assert gs_meta_2.access_token_encoded == new_access_token_encoded



@pytest.mark.asyncio
async def test_update_sync_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await db.run_sync(
		gs_meta_crud.create_sync,
		obj_in=gs_meta_in,
	)

	new_access_token_encoded = random_lower_string()

	gs_meta_in_update = GSMetaSchemaUpdate(
		access_token_encoded=new_access_token_encoded,
	)

	gs_meta_2 = await db.run_sync(
		gs_meta_crud.update_sync,
		db_obj=gs_meta,
		obj_in=gs_meta_in_update,
	)

	assert gs_meta_2
	assert gs_meta_2.access_token_encoded
	assert gs_meta_2.access_token_encoded == new_access_token_encoded



@pytest.mark.asyncio
async def test_delete_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await gs_meta_crud.create(
		db=db,
		obj_in=gs_meta_in,
	)

	gs_meta_2 = await gs_meta_crud.delete(
		db=db,
		id=gs_meta.id,
	)

	gs_meta_3 = await gs_meta_crud.get(
		db=db,
		id=gs_meta.id,
	)

	assert gs_meta_3 is None
	assert gs_meta_2.id == gs_meta.id




@pytest.mark.asyncio
async def test_delete_sync_gs_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()

	gs_meta_in = GSMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
	)

	gs_meta = await db.run_sync(
		gs_meta_crud.create_sync,
		obj_in=gs_meta_in,
	)

	gs_meta_2 = await db.run_sync(
		gs_meta_crud.delete_sync,
		id=gs_meta.id,
	)

	gs_meta_3 = await db.run_sync(
		gs_meta_crud.get_sync,
		id=gs_meta.id,
	)


	assert gs_meta_3 is None
	assert gs_meta_2.id == gs_meta.id



