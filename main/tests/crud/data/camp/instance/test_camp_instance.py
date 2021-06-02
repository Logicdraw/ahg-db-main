from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.instance import (
	camp_instance_crud,
)

from main.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	assert camp_instance.year_start == year_start
	assert camp_instance.se_name_snake = se_name_snake



@pytest.mark.asyncio
async def test_create_sync_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	assert camp_instance.year_start == year_start
	assert camp_instance.se_name_snake = se_name_snake



@pytest.mark.asyncio
async def test_get_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_2 = await camp_instance_crud.get(
		db=db,
		id=camp_instance.id,
	)


	assert camp_instance_2
	assert jsonable_encoder(camp_instance) == jsonable_encoder(camp_instance_2)




@pytest.mark.asyncio
async def test_get_sync_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_2 = await db.run_sync(
		camp_instance_crud.get_sync,
		id=camp_instance.id,
	)


	assert camp_instance_2
	assert jsonable_encoder(camp_instance) == jsonable_encoder(camp_instance_2)




@pytest.mark.asyncio
async def test_update_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)

	new_se_name_snake = random_lower_string()

	camp_instance_in_update = CampInstanceSchemaUpdate(
		se_name_snake=new_se_name_snake,
	)

	camp_instance_2 = await camp_instance_crud.update(
		db=db,
		db_obj=camp_instance,
		obj_in=camp_instance_in_update,
	)


	assert camp_instance_2
	assert camp_instance_2.se_name_snake
	assert camp_instance_2.se_name_snake == new_se_name_snake



@pytest.mark.asyncio
async def test_update_sync_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)

	new_se_name_snake = random_lower_string()

	camp_instance_in_update = CampInstanceSchemaUpdate(
		se_name_snake=new_se_name_snake,
	)

	camp_instance_2 = await db.run_sync(
		camp_instance_crud.update_sync,
		db_obj=camp_instance,
		obj_in=camp_instance_in_update,
	)


	assert camp_instance_2
	assert camp_instance_2.se_name_snake
	assert camp_instance_2.se_name_snake == new_se_name_snake



@pytest.mark.asyncio
async def test_delete_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_2 = await camp_instance_crud.delete(
		db=db,
		id=camp_instance.id,
	)


	camp_instance_3 = await camp_instance_crud.get(
		db=db,
		id=camp_instance.id,
	)


	assert camp_instance_3 is None
	assert camp_instance_2.id == camp_instance.id



@pytest.mark.asyncio
async def test_delete_sync_camp_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	se_name_snake = random_lower_string()
	se_shared_question_id = random_number()

	camp_instance_in = CampInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		se_name_snake=se_name_snake,
		se_shared_question_id=se_shared_question_id,
	)

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_2 = await db.run_sync(
		camp_instance_crud.delete_sync,
		id=camp_instance.id,
	)


	camp_instance_3 = await db.run_sync(
		camp_instance_crud.get_sync,
		id=camp_instance.id,
	)


	assert camp_instance_3 is None
	assert camp_instance_2.id == camp_instance.id





