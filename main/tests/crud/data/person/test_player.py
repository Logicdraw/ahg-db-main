from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.player import (
	player_crud,
)

from main.schemas.data.person.player import (
	PlayerSchemaCreate,
	PlayerSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_address,
	random_number,
)


import pytest


import datetime




@pytest.mark.asyncio
async def test_create_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)

	assert player
	assert player.first_name == first_name
	assert player.date_of_birth == date_of_birth
	# as_dict ... ? comes in handy??



@pytest.mark.asyncio
async def test_create_sync_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)

	assert player
	assert player.first_name == first_name
	assert player.date_of_birth == date_of_birth




@pytest.mark.asyncio
async def test_get_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)

	player_2 = await player_crud.get(
		db=db,
		id=player.id,
	)


	assert player_2
	assert jsonable_encoder(player) == jsonable_encoder(player_2)



@pytest.mark.asyncio
async def test_get_sync_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)

	player_2 = await db.run_sync(
		player_crud.get_sync,
		id=player.id,
	)

	assert player_2
	assert jsonable_encoder(player) == jsonable_encoder(player_2)




@pytest.mark.asyncio
async def test_update_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)

	new_first_name = random_name().split()[0]

	player_in_update = PlayerSchemaUpdate(
		first_name=new_first_name,
	)


	player_2 = await player_crud.update(
		db=db,
		db_obj=player,
		obj_in=player_in_update,
	)


	assert player_2
	assert player_2.first_name
	assert player_2.first_name == new_first_name



@pytest.mark.asyncio
async def test_update_sync_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	

	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)

	new_first_name = random_name().split()[0]

	player_in_update = PlayerSchemaUpdate(
		first_name=new_first_name,
	)


	player_2 = await db.run_sync(
		player_crud.update_sync,
		db_obj=player,
		obj_in=player_in_update,
	)


	assert player_2
	assert player_2.first_name
	assert player_2.first_name == new_first_name




@pytest.mark.asyncio
async def test_delete_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	
	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)

	player_2 = await player_crud.delete(
		db=db,
		id=player.id,
	)

	player_3 = await player_crud.get(
		db=db,
		id=player.id,
	)


	assert player_3 is None
	assert player_2.id == player.id




@pytest.mark.asyncio
async def test_delete_sync_player(
	db: AsyncSession,
) -> None:
	# --
	first_name = random_name().split()[0]
	last_name = random_name().split()[-1]
	email = random_email()
	date_of_birth: datetime.date = datetime.date.today()
	medicare_number = random_lower_string()
	street_address_1 = random_lower_string()
	street_address_2 = random_lower_string()
	postal_code = 'E1E 4N6'
	city = 'Moncton'
	province = 'NB'
	country = 'Canada'
	gender = 'male'
	spng_persona_id = random_number()
	
	player_in = PlayerSchemaCreate(
		first_name=first_name,
		last_name=last_name,
		email=email,
		date_of_birth=date_of_birth,
		medicare_number=medicare_number,
		street_address_1=street_address_1,
		street_address_2=street_address_2,
		postal_code=postal_code,
		city=city,
		province=province,
		country=country,
		gender=gender,
		spng_persona_id=spng_persona_id,
	)

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)

	player_2 = await db.run_sync(
		player_crud.delete_sync,
		id=player.id,
	)

	player_3 = await db.run_sync(
		player_crud.get_sync,
		id=player.id,
	)


	assert player_3 is None
	assert player_2.id == player.id





