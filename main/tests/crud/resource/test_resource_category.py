from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.resource.category import (
	resource_category_crud,
)

from main.schemas.resource.category import (
	ResourceCategorySchemaCreate,
	ResourceCategorySchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await resource_category_crud.create(
		db=db,
		obj_in=resource_category_in,
	)

	assert resource_category.name == name


@pytest.mark.asyncio
async def test_create_sync_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await db.run_sync(
		resource_category_crud.create_sync,
		obj_in=resource_category_in,
	)

	assert resource_category.name == name



@pytest.mark.asyncio
async def test_get_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await resource_category_crud.create(
		db=db,
		obj_in=resource_category_in,
	)

	resource_category_2 = await resource_category_crud.get(
		db=db,
		id=resource_category.id,
	)

	assert resource_category_2
	assert jsonable_encoder(resource_category_2) == jsonable_encoder(resource_category)



@pytest.mark.asyncio
async def test_get_sync_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await db.run_sync(
		resource_category_crud.create_sync,
		obj_in=resource_category_in,
	)

	resource_category_2 = await db.run_sync(
		resource_category_crud.get_sync,
		id=resource_category.id,
	)

	assert resource_category_2
	assert jsonable_encoder(resource_category_2) == jsonable_encoder(resource_category)



@pytest.mark.asyncio
async def test_update_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await resource_category_crud.create(
		db=db,
		obj_in=resource_category_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	resource_category_in_update = ResourceCategorySchemaUpdate(
		name=new_name,
	)

	resource_category_2 = await resource_category_crud.update(
		db=db,
		db_obj=resource_category,
		obj_in=resource_category_in_update,
	)

	assert resource_category_2
	assert resource_category_2.name
	assert resource_category_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await db.run_sync(
		resource_category_crud.create_sync,
		obj_in=resource_category_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	resource_category_in_update = ResourceCategorySchemaUpdate(
		name=new_name,
	)

	resource_category_2 = await db.run_sync(
		resource_category_crud.update_sync,
		db_obj=resource_category,
		obj_in=resource_category_in_update,
	)

	assert resource_category_2
	assert resource_category_2.name
	assert resource_category_2.name == new_name



@pytest.mark.asyncio
async def test_delete_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await resource_category_crud.create(
		db=db,
		obj_in=resource_category_in,
	)

	resource_category_2 = await resource_category_crud.delete(
		db=db,
		id=resource_category.id,
	)

	resource_category_3 = await resource_category_crud.get(
		db=db,
		id=resource_category.id,
	)

	assert resource_category_3 is None
	assert resource_category_2.id == resource_category.id



@pytest.mark.asyncio
async def test_delete_sync_resource_category(
	db: AsyncSession,
) -> None:
	# --
	is_live = True
	name = random_lower_string()
	slug = random_lower_string()

	resource_category_in = ResourceCategorySchemaCreate(
		is_live=is_live,
		name=name,
		slug=slug,
	)

	resource_category = await db.run_sync(
		resource_category_crud.create_sync,
		obj_in=resource_category_in,
	)

	resource_category_2 = await db.run_sync(
		resource_category_crud.delete_sync,
		id=resource_category.id,
	)

	resource_category_3 = await db.run_sync(
		resource_category_crud.get_sync,
		id=resource_category.id,
	)

	assert resource_category_3 is None
	assert resource_category_2.id == resource_category.id










