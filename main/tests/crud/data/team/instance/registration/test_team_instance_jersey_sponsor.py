from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.registration.jersey_sponsor import (
	team_instance_registration_jersey_sponsor_crud,
)

from main.schemas.data.team.instance.registration.jersey_sponsor import (
	TeamInstanceRegistrationJerseySponsorSchemaCreate,
	TeamInstanceRegistrationJerseySponsorSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	assert team_instance_registration_jersey_sponsor.name == name
	assert team_instance_registration_jersey_sponsor.amount == amount



@pytest.mark.asyncio
async def test_create_sync_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	assert team_instance_registration_jersey_sponsor.name == name
	assert team_instance_registration_jersey_sponsor.amount == amount




@pytest.mark.asyncio
async def test_get_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	team_instance_registration_jersey_sponsor_2 = await team_instance_registration_jersey_sponsor_crud.get(
		db=db,
		id=team_instance_registration_jersey_sponsor.id,
	)

	assert team_instance_registration_jersey_sponsor_2
	assert jsonable_encoder(team_instance_registration_jersey_sponsor_2) == jsonable_encoder(team_instance_registration_jersey_sponsor)



@pytest.mark.asyncio
async def test_get_sync_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	team_instance_registration_jersey_sponsor_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.get_sync,
		id=team_instance_registration_jersey_sponsor.id,
	)

	assert team_instance_registration_jersey_sponsor_2
	assert jsonable_encoder(team_instance_registration_jersey_sponsor_2) == jsonable_encoder(team_instance_registration_jersey_sponsor)




@pytest.mark.asyncio
async def test_update_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	team_instance_registration_jersey_sponsor_in_update = TeamInstanceRegistrationJerseySponsorSchemaUpdate(
		name=new_name,
	)

	team_instance_registration_jersey_sponsor_2 = await team_instance_registration_jersey_sponsor_crud.update(
		db=db,
		db_obj=team_instance_registration_jersey_sponsor,
		obj_in=team_instance_registration_jersey_sponsor_in_update,
	)

	assert team_instance_registration_jersey_sponsor_2
	assert team_instance_registration_jersey_sponsor_2.name
	assert team_instance_registration_jersey_sponsor_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	team_instance_registration_jersey_sponsor_in_update = TeamInstanceRegistrationJerseySponsorSchemaUpdate(
		name=new_name,
	)

	team_instance_registration_jersey_sponsor_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.update_sync,
		db_obj=team_instance_registration_jersey_sponsor,
		obj_in=team_instance_registration_jersey_sponsor_in_update,
	)

	assert team_instance_registration_jersey_sponsor_2
	assert team_instance_registration_jersey_sponsor_2.name
	assert team_instance_registration_jersey_sponsor_2.name == new_name



@pytest.mark.asyncio
async def test_delete_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	team_instance_registration_jersey_sponsor_2 = await team_instance_registration_jersey_sponsor_crud.delete(
		db=db,
		id=team_instance_registration_jersey_sponsor.id,
	)

	team_instance_registration_jersey_sponsor_3 = await team_instance_registration_jersey_sponsor_crud.get(
		db=db,
		id=team_instance_registration_jersey_sponsor.id,
	)

	assert team_instance_registration_jersey_sponsor_3 is None
	assert team_instance_registration_jersey_sponsor_2.id == team_instance_registration_jersey_sponsor.id




@pytest.mark.asyncio
async def test_delete_sync_team_instance_registration_jersey_sponsor(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = float(random_number(min_digits=3, max_digits=3)) # 100.0 - 999.0

	team_instance_registration_jersey_sponsor_in = TeamInstanceRegistrationJerseySponsorSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_registration_jersey_sponsor = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_registration_jersey_sponsor_in,
	)

	team_instance_registration_jersey_sponsor_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.delete_sync,
		id=team_instance_registration_jersey_sponsor.id,
	)

	team_instance_registration_jersey_sponsor_3 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.get_sync,
		id=team_instance_registration_jersey_sponsor.id,
	)

	assert team_instance_registration_jersey_sponsor_3 is None
	assert team_instance_registration_jersey_sponsor_2.id == team_instance_registration_jersey_sponsor.id




