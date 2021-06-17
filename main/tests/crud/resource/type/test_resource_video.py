from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.resource.video import (
	resource_video_crud,
)

from main.schemas.resource.video import (
	ResourceVideoSchemaCreate,
	ResourceVideoSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_resource_video(
	db: AsyncSession,
) -> None:
	# --
	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await resource_video_crud.create(
		db=db,
		obj_in=resource_video_in,
	)

	assert resource_video.video_url == video_url


@pytest.mark.asyncio
async def test_create_sync_resource_video(
	db: AsyncSession,
) -> None:
	# --
	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await db.run_sync(
		resource_video_crud.create_sync,
		obj_in=resource_video_in,
	)

	assert resource_video.video_url == video_url



@pytest.mark.asyncio
async def test_get_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await resource_video_crud.create(
		db=db,
		obj_in=resource_video_in,
	)

	resource_video_2 = await resource_video_crud.get(
		db=db,
		id=resource_video.id,
	)

	assert resource_video_2
	assert jsonable_encoder(resource_video_2) == jsonable_encoder(resource_video)



@pytest.mark.asyncio
async def test_get_sync_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await db.run_sync(
		resource_video_crud.create_sync,
		obj_in=resource_video_in,
	)

	resource_video_2 = await db.run_sync(
		resource_video_crud.get_sync,
		id=resource_video.id,
	)

	assert resource_video_2
	assert jsonable_encoder(resource_video_2) == jsonable_encoder(resource_video)



@pytest.mark.asyncio
async def test_update_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await resource_video_crud.create(
		db=db,
		obj_in=resource_video_in,
	)

	new_video_url = random_lower_string()
	while new_video_url == video_url:
		new_video_url = random_lower_string()

	resource_video_in_update = ResourceVideoSchemaUpdate(
		video_url=new_video_url,
	)

	resource_video_2 = await resource_video_crud.update(
		db=db,
		db_obj=resource_video,
		obj_in=resource_video_in_update,
	)

	assert resource_video_2
	assert resource_video_2.name
	assert resource_video_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await db.run_sync(
		resource_video_crud.create_sync,
		obj_in=resource_video_in,
	)

	new_video_url = random_lower_string()
	while new_video_url == video_url:
		new_video_url = random_lower_string()

	resource_video_in_update = ResourceVideoSchemaUpdate(
		video_url=new_video_url,
	)

	resource_video_2 = await db.run_sync(
		resource_video_crud.update_sync,
		db_obj=resource_video,
		obj_in=resource_video_in_update,
	)

	assert resource_video_2
	assert resource_video_2.name
	assert resource_video_2.name == new_name



@pytest.mark.asyncio
async def test_delete_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await resource_video_crud.create(
		db=db,
		obj_in=resource_video_in,
	)

	resource_video_2 = await resource_video_crud.delete(
		db=db,
		id=resource_video.id,
	)

	resource_video_3 = await resource_video_crud.get(
		db=db,
		id=resource_video.id,
	)

	assert resource_video_3 is None
	assert resource_video_2.id == resource_video.id



@pytest.mark.asyncio
async def test_delete_sync_resource_video(
	db: AsyncSession,
) -> None:
	# --

	video_url = random_lower_string()

	resource_video_in = ResourceVideoSchemaCreate(
		video_url=video_url,
	)

	resource_video = await db.run_sync(
		resource_video_crud.create_sync,
		obj_in=resource_video_in,
	)

	resource_video_2 = await db.run_sync(
		resource_video_crud.delete_sync,
		id=resource_video.id,
	)

	resource_video_3 = await db.run_sync(
		resource_video_crud.get_sync,
		id=resource_video.id,
	)

	assert resource_video_3 is None
	assert resource_video_2.id == resource_video.id






