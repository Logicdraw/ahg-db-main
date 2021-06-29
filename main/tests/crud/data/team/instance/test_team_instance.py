from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance import (
	team_instance_crud,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	assert team_instance.year_start == year_start
	assert team_instance.year_end == year_end
	assert team_instance.birth_year == birth_year
	assert team_instance.spng_name_snake == spng_name_snake
	assert team_instance.spng_shared_question_id == spng_shared_question_id
	assert team_instance.gs_team_id == gs_team_id
	assert team_instance.number_of_tracksuits_available == number_of_tracksuits_available
	assert team_instance.has_jersey_size_option == has_jersey_size_option
	assert team_instance.jersey_numbers_options == jersey_numbers_options
	assert team_instance.jersey_sizes_options == jersey_sizes_options
	assert team_instance.registrations_needs_jersey_default_value == registrations_needs_jersey_default_value
	assert team_instance.has_socks_size_option == has_socks_size_option
	assert team_instance.socks_sizes_options == socks_sizes_options
	assert team_instance.registrations_needs_socks_default_value == registrations_needs_socks_default_value



@pytest.mark.asyncio
async def test_create_sync_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	assert team_instance.year_start == year_start
	assert team_instance.year_end == year_end
	assert team_instance.birth_year == birth_year
	assert team_instance.spng_name_snake == spng_name_snake
	assert team_instance.spng_shared_question_id == spng_shared_question_id
	assert team_instance.gs_team_id == gs_team_id
	assert team_instance.number_of_tracksuits_available == number_of_tracksuits_available
	assert team_instance.has_jersey_size_option == has_jersey_size_option
	assert team_instance.jersey_numbers_options == jersey_numbers_options
	assert team_instance.jersey_sizes_options == jersey_sizes_options
	assert team_instance.registrations_needs_jersey_default_value == registrations_needs_jersey_default_value
	assert team_instance.has_socks_size_option == has_socks_size_option
	assert team_instance.socks_sizes_options == socks_sizes_options
	assert team_instance.registrations_needs_socks_default_value == registrations_needs_socks_default_value




@pytest.mark.asyncio
async def test_get_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)

	team_instance_2 = await team_instance_crud.get(
		db=db,
		id=team_instance.id,
	)

	assert team_instance_2
	assert jsonable_encoder(team_instance_2) == jsonable_encoder(team_instance)
	


@pytest.mark.asyncio
async def test_get_sync_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)

	team_instance_2 = await db.run_sync(
		team_instance_crud.get_sync,
		id=team_instance.id,
	)

	assert team_instance_2
	assert jsonable_encoder(team_instance_2) == jsonable_encoder(team_instance)
	



@pytest.mark.asyncio
async def test_update_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)


	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	new_spng_name_snake = random_lower_string()
	while new_spng_name_snake == spng_name_snake:
		spng_name_snake = random_lower_string()


	team_instance_in_update = TeamInstanceSchemaUpdate(
		spng_name_snake=new_spng_name_snake,
	)

	team_instance_2 = await team_instance_crud.update(
		db=db,
		db_obj=team_instance,
		obj_in=team_instance_in_update,
	)

	assert team_instance_2
	assert team_instance_2.spng_name_snake
	assert team_instance_2.spng_name_snake == new_spng_name_snake



@pytest.mark.asyncio
async def test_update_sync_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)


	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	new_spng_name_snake = random_lower_string()
	while new_spng_name_snake == spng_name_snake:
		spng_name_snake = random_lower_string()


	team_instance_in_update = TeamInstanceSchemaUpdate(
		spng_name_snake=new_spng_name_snake,
	)

	team_instance_2 = await db.run_sync(
		team_instance_crud.update_sync,
		db_obj=team_instance,
		obj_in=team_instance_in_update,
	)

	assert team_instance_2
	assert team_instance_2.spng_name_snake
	assert team_instance_2.spng_name_snake == new_spng_name_snake



@pytest.mark.asyncio
async def test_delete_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)


	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)

	team_instance_2 = await team_instance_crud.delete(
		db=db,
		id=team_instance.id,
	)

	team_instance_3 = await team_instance_crud.get(
		db=db,
		id=team_instance.id,
	)

	assert team_instance_3 is None
	assert team_instance_2.id == team_instance.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	birth_year = 2010

	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	gs_team_id = random_number()

	number_of_tracksuits_available = random_number()

	has_jersey_size_option = True
	jersey_numbers_options = '0:68-70:99' # Exclude 69 -- (Example)
	jersey_sizes_options = '9-M:6-L:2-L!G'
	registrations_needs_jersey_default_value = False

	has_socks_size_option = True
	socks_sizes_options = 'i-24in:i-26in'
	registrations_needs_socks_default_value = False

	
	team_instance_in = TeamInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		birth_year=birth_year,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
		gs_team_id=gs_team_id,
		number_of_tracksuits_available=number_of_tracksuits_available,
		has_jersey_size_option=has_jersey_size_option,
		jersey_numbers_options=jersey_numbers_options,
		jersey_sizes_options=jersey_sizes_options,
		registrations_needs_jersey_default_value=registrations_needs_jersey_default_value,
		has_socks_size_option=has_socks_size_option,
		socks_sizes_options=socks_sizes_options,
		registrations_needs_socks_default_value=registrations_needs_socks_default_value,
	)


	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)

	team_instance_2 = await db.run_sync(
		team_instance_crud.delete_sync,
		id=team_instance.id,
	)

	team_instance_3 = await db.run_sync(
		team_instance_crud.get_sync,
		id=team_instance.id,
	)

	assert team_instance_3 is None
	assert team_instance_2.id == team_instance.id






