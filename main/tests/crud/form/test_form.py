from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form import (
	form_crud,
)

from main.schemas.form import (
	FormSchemaCreate,
	FormSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest


import pytz

import datetime





@pytest.mark.asyncio
async def test_create_form(
	db: AsyncSession,
) -> None:
	# --
	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await form_crud.create(
		db=db,
		obj_in=form_in,
	)

	assert form.title == title
	assert form.description == description
	assert form.has_deadline == has_deadline
	assert form.deadline_on == deadline_on



@pytest.mark.asyncio
async def test_create_sync_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await db.run_sync(
		form_crud.create_sync,
		obj_in=form_in,
	)

	assert form.title == title
	assert form.description == description
	assert form.has_deadline == has_deadline
	assert form.deadline_on == deadline_on



@pytest.mark.asyncio
async def test_get_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await form_crud.create(
		db=db,
		obj_in=form_in,
	)

	form_2 = await form_crud.get(
		db=db,
		id=form.id,
	)

	assert form_2
	assert jsonable_encoder(form_2) == jsonable_encoder(form)



@pytest.mark.asyncio
async def test_get_sync_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await db.run_sync(
		form_crud.create_sync,
		obj_in=form_in,
	)

	form_2 = await db.run_sync(
		form_crud.get_sync,
		id=form.id,
	)

	assert form_2
	assert jsonable_encoder(form_2) == jsonable_encoder(form)



@pytest.mark.asyncio
async def test_update_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await form_crud.create(
		db=db,
		obj_in=form_in,
	)

	new_title = random_lower_string()
	while new_title == title:
		new_title = random_lower_string()


	form_in_update = FormSchemaUpdate(
		title=new_title,
	)


	form_2 = await form_crud.update(
		db=db,
		db_obj=form,
		obj_in=form_in_update,
	)

	assert form_2
	assert form_2.title
	assert form_2.title == new_title



@pytest.mark.asyncio
async def test_update_sync_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await db.run_sync(
		form_crud.create_sync,
		obj_in=form_in,
	)

	new_title = random_lower_string()
	while new_title == title:
		new_title = random_lower_string()

	form_in_update = FormSchemaUpdate(
		title=new_title,
	)

	form_2 = await db.run_sync(
		form_crud.update_sync,
		db_obj=form,
		obj_in=form_in_update,
	)

	assert form_2
	assert form_2.title
	assert form_2.title == new_title




@pytest.mark.asyncio
async def test_delete_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await form_crud.create(
		db=db,
		obj_in=form_in,
	)

	form_2 = await form_crud.delete(
		db=db,
		id=form.id,
	)

	form_3 = await form_crud.get(
		db=db,
		id=form.id,
	)


	assert form_3 is None
	assert form_2.id == form.id



@pytest.mark.asyncio
async def test_delete_sync_form(
	db: AsyncSession,
) -> None:
	# --

	title = random_lower_string()
	description = random_lower_string()
	has_deadline = True
	deadline_on = datetime.datetime.now(pytz.utc)

	form_in = FormSchemaCreate(
		title=title,
		description=description,
		has_deadline=has_deadline,
		deadline_on=deadline_on,
	)

	form = await db.run_sync(
		form_crud.create_sync,
		obj_in=form_in,
	)

	form_2 = await db.run_sync(
		form_crud.delete_sync,
		id=form.id,
	)

	form_3 = await db.run_sync(
		form_crud.get_sync,
		id=form.id,
	)


	assert form_3 is None
	assert form_2.id == form.id




