from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._base.resource import (
	resource_base_crud,
)

from main.schemas._base.resource import (
	ResourceBaseSchemaCreate,
	ResourceBaseSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)

import pytest



@pytest.mark.asyncio
async def test_create_resource_base(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await resource_base_crud.create(
		db=db,
		obj_in=resource_base_in,
	)

	assert resource_base.survey_id == survey_id
	assert resource_base.name == name



@pytest.mark.asyncio
async def test_create_sync_resource_base(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await db.run_sync(
		resource_base_crud.create_sync,
		obj_in=resource_base_in,
	)

	assert resource_base.survey_id == survey_id
	assert resource_base.name == name



@pytest.mark.asyncio
async def test_get_resource_base(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await resource_base_crud.create(
		db=db,
		obj_in=resource_base_in,
	)

	resource_base_2 = await resource_base_crud.get(
		db=db,
		id=resource_base.id,
	)


	assert resource_base_2
	assert jsonable_encoder(resource_base) == jsonable_encoder(resource_base_2)



@pytest.mark.asyncio
async def test_get_sync_resource_base(
	db: AsyncSession,
) -> None:
	# --

	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await db.run_sync(
		resource_base_crud.create_sync,
		obj_in=resource_base_in,
	)

	resource_base_2 = await db.run_sync(
		resource_base_crud.get_sync,
		id=resource_base.id,
	)


	assert resource_base_2
	assert jsonable_encoder(resource_base) == jsonable_encoder(resource_base_2)





@pytest.mark.asyncio
async def test_update_resource_base(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await resource_base_crud.create(
		db=db,
		obj_in=resource_base_in,
	)


	new_name = random_name()
	while new_name == name:
		new_name = random_name()

	resource_base_in_update = ResourceBaseSchemaUpdate(
		name=new_name,
	)

	resource_base_2 = await resource_base_crud.update(
		db=db,
		db_obj=resource_base,
		obj_in=resource_base_in_update,
	)


	assert resource_base_2
	assert resource_base_2.name
	assert resource_base_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_resource_base(
	db: AsyncSession,
) -> None:
	# --

	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await db.run_sync(
		resource_base_crud.create_sync,
		obj_in=resource_base_in,
	)

	new_name = random_name()
	while new_name == name:
		new_name = random_name()

	resource_base_in_update = ResourceBaseSchemaUpdate(
		name=new_name,
	)

	resource_base_2 = await db.run_sync(
		resource_base_crud.update_sync,
		db_obj=resource_base,
		obj_in=resource_base_in_update,
	)


	assert resource_base_2
	assert resource_base_2.name
	assert resource_base_2.name == new_name



@pytest.mark.asyncio
async def test_delete_resource_base(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await resource_base_crud.create(
		db=db,
		obj_in=resource_base_in,
	)

	resource_base_2 = await resource_base_crud.delete(
		db=db,
		id=resource_base.id,
	)

	resource_base_3 = await resource_base_crud.get(
		db=db,
		id=resource_base.id,
	)


	assert resource_base_3 is None
	assert resource_base_2.id == resource_base.id




@pytest.mark.asyncio
async def test_delete_sync_resource_base(
	db: AsyncSession,
) -> None:
	# --

	is_live = True
	name = random_lower_string()
	slug = random_lower_string()
	thumbnail_image_url = random_lower_string()
	type = 'other'

	resource_base_in = ResourceBaseSchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
		thumbnail_image_url=thumbnail_image_url,
		type=type,
	)
	resource_base = await db.run_sync(
		resource_base_crud.create_sync,
		obj_in=resource_base_in,
	)

	resource_base_2 = await db.run_sync(
		resource_base_crud.delete_sync,
		id=resource_base.id,
	)

	resource_base_3 = await db.run_sync(
		resource_base_crud.get_sync,
		id=resource_base.id,
	)


	assert resource_base_3 is None
	assert resource_base_2.id == resource_base.id






