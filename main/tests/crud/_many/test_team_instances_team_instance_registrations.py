from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.team_instances_team_instance_registrations import (
	team_instances_team_instance_registrations_crud,
)

from main.schemas._many.team_instances_team_instance_registrations import (
	TeamInstancesTeamInstanceRegistrationsSchemaCreate,
	TeamInstancesTeamInstanceRegistrationsSchemaUpdate,
)



from main.crud.data.team.instance import (
	team_instance_crud,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)



from main.crud.data.team.instance.registration import (
	team_instance_registration_crud,
)

from main.schemas.data.team.instance.registration import (
	TeamInstanceRegistrationSchemaCreate,
	TeamInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await team_instance_registration_crud.create(
		db=db,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await team_instances_team_instance_registrations_crud.create(
		db=db,
		obj_in=team_instance_team_instance_registration_in,
	)


	assert team_instance_team_instance_registration.team_instance_id == team_instance.id
	assert team_instance_team_instance_registration.team_instance_registration_id == team_instance_registration.id



@pytest.mark.asyncio
async def test_create_sync_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await db.run_sync(
		team_instance_registration_crud.create_sync,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await db.run_sync(
		team_instances_team_instance_registrations_crud.create_sync,
		obj_in=team_instance_team_instance_registration_in,
	)


	assert team_instance_team_instance_registration.team_instance_id == team_instance.id
	assert team_instance_team_instance_registration.team_instance_registration_id == team_instance_registration.id



@pytest.mark.asyncio
async def test_get_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await team_instance_registration_crud.create(
		db=db,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await team_instances_team_instance_registrations_crud.create(
		db=db,
		obj_in=team_instance_team_instance_registration_in,
	)


	team_instance_team_instance_registration_2 = await team_instances_team_instance_registrations_crud.get(
		db=db,
		team_instance_id=team_instance_team_instance_registration.team_instance_id,
		team_instance_registration_id=team_instance_team_instance_registration.team_instance_registration_id,
	)

	assert team_instance_team_instance_registration_2
	assert jsonable_encoder(team_instance_team_instance_registration) == jsonable_encoder(team_instance_team_instance_registration_2)



@pytest.mark.asyncio
async def test_get_sync_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await db.run_sync(
		team_instance_registration_crud.create_sync,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await db.run_sync(
		team_instances_team_instance_registrations_crud.create_sync,
		obj_in=team_instance_team_instance_registration_in,
	)


	team_instance_team_instance_registration_2 = await db.run_sync(
		team_instances_team_instance_registrations_crud.get_sync,
		team_instance_id=team_instance_team_instance_registration.team_instance_id,
		team_instance_registration_id=team_instance_team_instance_registration.team_instance_registration_id,
	)

	assert team_instance_team_instance_registration_2
	assert jsonable_encoder(team_instance_team_instance_registration) == jsonable_encoder(team_instance_team_instance_registration_2)



@pytest.mark.asyncio
async def test_update_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await team_instance_registration_crud.create(
		db=db,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await team_instances_team_instance_registrations_crud.create(
		db=db,
		obj_in=team_instance_team_instance_registration_in,
	)


	team_instance_team_instance_registration_in_update = TeamInstancesTeamInstanceRegistrationsSchemaUpdate()

	team_instance_team_instance_registration_2 = await team_instances_team_instance_registrations_crud.update(
		db=db,
		db_obj=team_instance_team_instance_registration,
		obj_in=team_instance_team_instance_registration_in_update,
	)

	assert team_instance_team_instance_registration_2




@pytest.mark.asyncio
async def test_update_sync_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await db.run_sync(
		team_instance_registration_crud.create_sync,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await db.run_sync(
		team_instances_team_instance_registrations_crud.create_sync,
		obj_in=team_instance_team_instance_registration_in,
	)



	team_instance_team_instance_registration_in_update = TeamInstancesTeamInstanceRegistrationsSchemaUpdate()

	team_instance_team_instance_registration_2 = await db.run_sync(
		team_instances_team_instance_registrations_crud.update_sync,
		db_obj=team_instance_team_instance_registration,
		obj_in=team_instance_team_instance_registration_in_update,
	)

	assert team_instance_team_instance_registration_2




@pytest.mark.asyncio
async def test_delete_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await team_instance_registration_crud.create(
		db=db,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await team_instances_team_instance_registrations_crud.create(
		db=db,
		obj_in=team_instance_team_instance_registration_in,
	)

	team_instance_team_instance_registration_2 = await team_instances_team_instance_registrations_crud.delete(
		db=db,
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration_3 = await team_instances_team_instance_registrations_crud.get(
		db=db,
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	assert team_instance_team_instance_registration_3 is None
	assert team_instance_team_instance_registration_2.team_instance_id == team_instance_team_instance_registration.team_instance_id
	assert team_instance_team_instance_registration_2.team_instance_registration_id == team_instance_team_instance_registration.team_instance_registration_id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_team_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	team_instance_registration_in = TeamInstanceRegistrationSchemaCreate()

	team_instance_registration = await db.run_sync(
		team_instance_registration_crud.create_sync,
		obj_in=team_instance_registration_in,
	)


	team_instance_team_instance_registration_in = TeamInstancesTeamInstanceRegistrationsSchemaCreate(
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration = await db.run_sync(
		team_instances_team_instance_registrations_crud.create_sync,
		obj_in=team_instance_team_instance_registration_in,
	)

	team_instance_team_instance_registration_2 = await db.run_sync(
		team_instances_team_instance_registrations_crud.delete_sync,
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	team_instance_team_instance_registration_3 = await db.run_sync(
		team_instances_team_instance_registrations_crud.get_sync,
		team_instance_id=team_instance.id,
		team_instance_registration_id=team_instance_registration.id,
	)

	assert team_instance_team_instance_registration_3 is None
	assert team_instance_team_instance_registration_2.team_instance_id == team_instance_team_instance_registration.team_instance_id
	assert team_instance_team_instance_registration_2.team_instance_registration_id == team_instance_team_instance_registration.team_instance_registration_id





