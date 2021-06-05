from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.meta.spng import (
	spng_meta_crud,
)

from main.schemas.meta.spng import (
	SpngMetaSchemaCreate,
	SpngMetaSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await spng_meta_crud.create(
		db=db,
		obj_in=spng_meta_in,
	)

	assert spng_meta.access_token_encoded == access_token_encoded
	assert spng_meta.refresh_token_encoded == refresh_token_encoded




@pytest.mark.asyncio
async def test_create_sync_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await db.run_sync(
		spng_meta_crud.create_sync,
		obj_in=spng_meta_in,
	)

	assert spng_meta.access_token_encoded == access_token_encoded
	assert spng_meta.refresh_token_encoded == refresh_token_encoded



@pytest.mark.asyncio
async def test_get_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await spng_meta_crud.create(
		db=db,
		obj_in=spng_meta_in,
	)

	spng_meta_2 = await spng_meta_crud.get(
		db=db,
		id=spng_meta.id,
	)

	assert spng_meta_2
	assert jsonable_encoder(spng_meta_2) == jsonable_encoder(spng_meta)



@pytest.mark.asyncio
async def test_get_sync_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await db.run_sync(
		spng_meta_crud.create_sync,
		obj_in=spng_meta_in,
	)

	spng_meta_2 = await db.run_sync(
		spng_meta_crud.get_sync,
		id=spng_meta.id,
	)

	assert spng_meta_2
	assert jsonable_encoder(spng_meta_2) == jsonable_encoder(spng_meta)



@pytest.mark.asyncio
async def test_update_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await spng_meta_crud.create(
		db=db,
		obj_in=spng_meta_in,
	)


	new_access_token_encoded = random_lower_string()

	spng_meta_in_update = SpngMetaSchemaUpdate(
		access_token_encoded=new_access_token_encoded,
	)

	spng_meta_2 = await spng_meta_crud.update(
		db=db,
		db_obj=spng_meta,
		obj_in=spng_meta_in_update,
	)


	assert spng_meta_2
	assert spng_meta_2.access_token_encoded
	assert spng_meta_2.access_token_encoded == new_access_token_encoded


@pytest.mark.asyncio
async def test_update_sync_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await db.run_sync(
		spng_meta_crud.create_sync,
		obj_in=spng_meta_in,
	)


	new_access_token_encoded = random_lower_string()

	spng_meta_in_update = SpngMetaSchemaUpdate(
		access_token_encoded=new_access_token_encoded,
	)

	spng_meta_2 = await db.run_sync(
		spng_meta_crud.update_sync,
		db_obj=spng_meta,
		obj_in=spng_meta_in_update,
	)

	assert spng_meta_2
	assert spng_meta_2.access_token_encoded
	assert spng_meta_2.access_token_encoded == new_access_token_encoded



@pytest.mark.asyncio
async def test_delete_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await spng_meta_crud.create(
		db=db,
		obj_in=spng_meta_in,
	)

	spng_meta_2 = await spng_meta_crud.delete(
		db=db,
		id=spng_meta.id,
	)

	spng_meta_3 = await spng_meta_crud.get(
		db=db,
		id=spng_meta.id,
	)


	assert spng_meta_3 is None
	assert spng_meta_2.id == spng_meta.id



@pytest.mark.asyncio
async def test_delete_sync_spng_meta(
	db: AsyncSession,
) -> None:
	# --
	access_token_encoded = random_lower_string()
	refresh_token_encoded = random_lower_string()

	spng_meta_in = SpngMetaSchemaCreate(
		access_token_encoded=access_token_encoded,
		refresh_token_encoded=refresh_token_encoded,
	)

	spng_meta = await db.run_sync(
		spng_meta_crud.create_sync,
		obj_in=spng_meta_in,
	)

	spng_meta_2 = await db.run_sync(
		spng_meta_crud.delete_sync,
		id=spng_meta.id,
	)

	spng_meta_3 = await db.run_sync(
		spng_meta_crud.get_sync,
		id=spng_meta.id,
	)

	
	assert spng_meta_3 is None
	assert spng_meta_2.id == spng_meta.id





