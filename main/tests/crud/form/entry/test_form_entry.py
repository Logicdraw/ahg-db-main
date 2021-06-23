from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form.entry import (
	form_entry_crud,
)

from main.schemas.form.entry import (
	FormEntrySchemaCreate,
	FormEntrySchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest


import datetime

import pytz





@pytest.mark.asyncio
async def test_create_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await form_entry_crud.create(
		db=db,
		obj_in=form_entry_in,
	)

	assert form_entry.id



@pytest.mark.asyncio
async def test_create_sync_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await db.run_sync(
		form_entry_crud.create_sync,
		obj_in=form_entry_in,
	)

	assert form_entry.id



@pytest.mark.asyncio
async def test_get_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await form_entry_crud.create(
		db=db,
		obj_in=form_entry_in,
	)

	form_entry_2 = await form_entry_crud.get(
		db=db,
		id=form_entry.id,
	)

	assert form_entry_2
	assert jsonable_encoder(form_entry_2) == jsonable_encoder(form_entry)



@pytest.mark.asyncio
async def test_get_sync_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await db.run_sync(
		form_entry_crud.create_sync,
		obj_in=form_entry_in,
	)

	form_entry_2 = await db.run_sync(
		form_entry_crud.get_sync,
		id=form_entry.id,
	)

	assert form_entry_2
	assert jsonable_encoder(form_entry_2) == jsonable_encoder(form_entry)



@pytest.mark.asyncio
async def test_update_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await form_entry_crud.create(
		db=db,
		obj_in=form_entry_in,
	)

	form_entry_in_update = FormEntrySchemaUpdate()

	form_entry_2 = await form_entry_crud.update(
		db=db,
		db_obj=form_entry,
		obj_in=form_entry_in_update,
	)

	assert form_entry_2
	# ??



@pytest.mark.asyncio
async def test_update_sync_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await db.run_sync(
		form_entry_crud.create_sync,
		obj_in=form_entry_in,
	)

	form_entry_in_update = FormEntrySchemaUpdate()

	form_entry_2 = await db.run_sync(
		form_entry_crud.update_sync,
		db_obj=form_entry,
		obj_in=form_entry_in_update,
	)

	assert form_entry_2
	# ??


@pytest.mark.asyncio
async def test_delete_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await form_entry_crud.create(
		db=db,
		obj_in=form_entry_in,
	)

	form_entry_2 = await form_entry_crud.delete(
		db=db,
		id=form_entry.id,
	)

	form_entry_3 = await form_entry_crud.get(
		db=db,
		id=form_entry.id,
	)


	assert form_entry_3 is None
	assert form_entry_2.id == form_entry.id



@pytest.mark.asyncio
async def test_delete_sync_form_entry(
	db: AsyncSession,
) -> None:
	# --

	slug = random_lower_string()

	form_entry_in = FormEntrySchemaCreate(
		slug=slug,
	)

	form_entry = await db.run_sync(
		form_entry_crud.create_sync,
		obj_in=form_entry_in,
	)

	form_entry_2 = await db.run_sync(
		form_entry_crud.delete_sync,
		id=form_entry.id,
	)

	form_entry_3 = await db.run_sync(
		form_entry_crud.get_sync,
		id=form_entry.id,
	)


	assert form_entry_3 is None
	assert form_entry_2.id == form_entry.id



