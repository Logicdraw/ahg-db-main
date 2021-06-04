from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.team_instances_coaches import (
	team_instances_coaches_crud,
)

from main.schemas._many.team_instances_coaches import (
	TeamInstancesCoachesSchemaCreate,
	TeamInstancesCoachesSchemaUpdate,
)



from main.crud.data.team.instance import (
	team_instance_crud,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)


from main.crud.data.person.coach import (
	coach_crud,
)

from main.schemas.data.person.coach import (
	CoachSchemaCreate,
	CoachSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



import pytest





@pytest.mark.asyncio
async def test_create_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await team_instances_coaches_crud.create(
		db=db,
		obj_in=team_instance_coach_in,
	)


	assert team_instance_coach.team_instance_id == team_instance.id
	assert team_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_create_sync_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await db.run_sync(
		team_instances_coaches_crud.create_sync,
		obj_in=team_instance_coach_in,
	)


	assert team_instance_coach.team_instance_id == team_instance.id
	assert team_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_get_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await team_instances_coaches_crud.create(
		db=db,
		obj_in=team_instance_coach_in,
	)


	team_instance_coach_2 = await team_instances_coaches_crud.get(
		db=db,
		team_instance_id=team_instance_coach.team_instance_id,
		coach_id=team_instance_coach.coach_id,
	)

	assert team_instance_coach_2
	assert jsonable_encoder(team_instance_coach) == jsonable_encoder(team_instance_coach_2)



@pytest.mark.asyncio
async def test_get_sync_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await db.run_sync(
		team_instances_coaches_crud.create_sync,
		obj_in=team_instance_coach_in,
	)


	team_instance_coach_2 = await db.run_sync(
		team_instances_coaches_crud.get_sync,
		team_instance_id=team_instance_coach.team_instance_id,
		coach_id=team_instance_coach.coach_id,
	)

	assert team_instance_coach_2
	assert jsonable_encoder(team_instance_coach) == jsonable_encoder(team_instance_coach_2)



@pytest.mark.asyncio
async def test_update_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await team_instances_coaches_crud.create(
		db=db,
		obj_in=team_instance_coach_in,
	)

	new_role = 'apple'

	team_instance_coach_in_update = TeamInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	team_instance_coach_2 = await team_instances_coaches_crud.update(
		db=db,
		db_obj=team_instance_coach,
		obj_in=team_instance_coach_in_update,
	)

	assert team_instance_coach_2
	assert team_instance_coach_2.role is not None
	assert team_instance_coach_2.role == new_role




@pytest.mark.asyncio
async def test_update_sync_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await db.run_sync(
		team_instances_coaches_crud.create_sync,
		obj_in=team_instance_coach_in,
	)


	new_role = 'apple'

	team_instance_coach_in_update = TeamInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	team_instance_coach_2 = await db.run_sync(
		team_instances_coaches_crud.update_sync,
		db_obj=team_instance_coach,
		obj_in=team_instance_coach_in_update,
	)

	assert team_instance_coach_2
	assert team_instance_coach_2.role is not None
	assert team_instance_coach_2.role == new_role




@pytest.mark.asyncio
async def test_delete_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await team_instances_coaches_crud.create(
		db=db,
		obj_in=team_instance_coach_in,
	)

	team_instance_coach_2 = await team_instances_coaches_crud.delete(
		db=db,
		team_instance_id=team_instance.id,
		coach_id=coach.id,
	)

	team_instance_coach_3 = await team_instances_coaches_crud.get(
		db=db,
		team_instance_id=team_instance.id,
		coach_id=coach.id,
	)

	assert team_instance_coach_3 is None
	assert team_instance_coach_2.team_instance_id == team_instance_coach.team_instance_id
	assert team_instance_coach_2.coach_id == team_instance_coach.coach_id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	team_instance_coach_in = TeamInstancesCoachesSchemaCreate(
		team_instance_id=team_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	team_instance_coach = await db.run_sync(
		team_instances_coaches_crud.create_sync,
		obj_in=team_instance_coach_in,
	)

	team_instance_coach_2 = await db.run_sync(
		team_instances_coaches_crud.delete_sync,
		team_instance_id=team_instance.id,
		coach_id=coach.id,
	)

	team_instance_coach_3 = await db.run_sync(
		team_instances_coaches_crud.get_sync,
		team_instance_id=team_instance.id,
		coach_id=coach.id,
	)

	assert team_instance_coach_3 is None
	assert team_instance_coach_2.team_instance_id == team_instance_coach.team_instance_id
	assert team_instance_coach_2.coach_id == team_instance_coach.coach_id





