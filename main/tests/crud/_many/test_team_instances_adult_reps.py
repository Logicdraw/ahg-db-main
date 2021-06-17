from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.team_instances_adult_reps import (
	team_instances_adult_reps_crud,
)

from main.schemas._many.team_instances_adult_reps import (
	TeamInstancesAdultRepsSchemaCreate,
	TeamInstancesAdultRepsSchemaUpdate,
)



from main.crud.data.team.instance import (
	team_instance_crud,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)


from main.crud.data.person.adult_rep import (
	adult_rep_crud,
)

from main.schemas.data.person.adult_rep import (
	AdultRepSchemaCreate,
	AdultRepSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



import pytest





@pytest.mark.asyncio
async def test_create_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await team_instances_adult_reps_crud.create(
		db=db,
		obj_in=team_instance_adult_rep_in,
	)


	assert team_instance_adult_rep.team_instance_id == team_instance.id
	assert team_instance_adult_rep.adult_rep_id == adult_rep.id



@pytest.mark.asyncio
async def test_create_sync_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await db.run_sync(
		team_instances_adult_reps_crud.create_sync,
		obj_in=team_instance_adult_rep_in,
	)


	assert team_instance_adult_rep.team_instance_id == team_instance.id
	assert team_instance_adult_rep.adult_rep_id == adult_rep.id



@pytest.mark.asyncio
async def test_get_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await team_instances_adult_reps_crud.create(
		db=db,
		obj_in=team_instance_adult_rep_in,
	)


	team_instance_adult_rep_2 = await team_instances_adult_reps_crud.get(
		db=db,
		team_instance_id=team_instance_adult_rep.team_instance_id,
		adult_rep_id=team_instance_adult_rep.adult_rep_id,
	)

	assert team_instance_adult_rep_2
	assert jsonable_encoder(team_instance_adult_rep) == jsonable_encoder(team_instance_adult_rep_2)



@pytest.mark.asyncio
async def test_get_sync_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await db.run_sync(
		team_instances_adult_reps_crud.create_sync,
		obj_in=team_instance_adult_rep_in,
	)


	team_instance_adult_rep_2 = await db.run_sync(
		team_instances_adult_reps_crud.get_sync,
		team_instance_id=team_instance_adult_rep.team_instance_id,
		adult_rep_id=team_instance_adult_rep.adult_rep_id,
	)

	assert team_instance_adult_rep_2
	assert jsonable_encoder(team_instance_adult_rep) == jsonable_encoder(team_instance_adult_rep_2)



@pytest.mark.asyncio
async def test_update_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await team_instances_adult_reps_crud.create(
		db=db,
		obj_in=team_instance_adult_rep_in,
	)

	new_role = 'apple'

	team_instance_adult_rep_in_update = TeamInstancesAdultRepsSchemaUpdate(
		role=new_role,
	)

	team_instance_adult_rep_2 = await team_instances_adult_reps_crud.update(
		db=db,
		db_obj=team_instance_adult_rep,
		obj_in=team_instance_adult_rep_in_update,
	)

	assert team_instance_adult_rep_2
	assert team_instance_adult_rep_2.role is not None
	assert team_instance_adult_rep_2.role == new_role




@pytest.mark.asyncio
async def test_update_sync_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await db.run_sync(
		team_instances_adult_reps_crud.create_sync,
		obj_in=team_instance_adult_rep_in,
	)


	new_role = 'apple'

	team_instance_adult_rep_in_update = TeamInstancesAdultRepsSchemaUpdate(
		role=new_role,
	)

	team_instance_adult_rep_2 = await db.run_sync(
		team_instances_adult_reps_crud.update_sync,
		db_obj=team_instance_adult_rep,
		obj_in=team_instance_adult_rep_in_update,
	)

	assert team_instance_adult_rep_2
	assert team_instance_adult_rep_2.role is not None
	assert team_instance_adult_rep_2.role == new_role




@pytest.mark.asyncio
async def test_delete_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await team_instances_adult_reps_crud.create(
		db=db,
		obj_in=team_instance_adult_rep_in,
	)

	team_instance_adult_rep_2 = await team_instances_adult_reps_crud.delete(
		db=db,
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
	)

	team_instance_adult_rep_3 = await team_instances_adult_reps_crud.get(
		db=db,
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
	)

	assert team_instance_adult_rep_3 is None
	assert team_instance_adult_rep_2.team_instance_id == team_instance_adult_rep.team_instance_id
	assert team_instance_adult_rep_2.adult_rep_id == team_instance_adult_rep.adult_rep_id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_adult_rep(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	adult_rep_in = AdultRepSchemaCreate()

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)


	team_instance_adult_rep_in = TeamInstancesAdultRepsSchemaCreate(
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
		role='banana',
	)

	team_instance_adult_rep = await db.run_sync(
		team_instances_adult_reps_crud.create_sync,
		obj_in=team_instance_adult_rep_in,
	)

	team_instance_adult_rep_2 = await db.run_sync(
		team_instances_adult_reps_crud.delete_sync,
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
	)

	team_instance_adult_rep_3 = await db.run_sync(
		team_instances_adult_reps_crud.get_sync,
		team_instance_id=team_instance.id,
		adult_rep_id=adult_rep.id,
	)

	assert team_instance_adult_rep_3 is None
	assert team_instance_adult_rep_2.team_instance_id == team_instance_adult_rep.team_instance_id
	assert team_instance_adult_rep_2.adult_rep_id == team_instance_adult_rep.adult_rep_id





