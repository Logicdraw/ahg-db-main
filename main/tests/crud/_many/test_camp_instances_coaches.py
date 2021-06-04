from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.camp_instances_coaches import (
	camp_instances_coaches_crud,
)

from main.schemas._many.camp_instances_coaches import (
	CampInstancesCoachesSchemaCreate,
	CampInstancesCoachesSchemaUpdate,
)



from main.crud.data.camp.instance import (
	camp_instance_crud,
)

from main.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
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
async def test_create_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await camp_instances_coaches_crud.create(
		db=db,
		obj_in=camp_instance_coach_in,
	)


	assert camp_instance_coach.camp_instance_id == camp_instance.id
	assert camp_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_create_sync_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await db.run_sync(
		camp_instances_coaches_crud.create_sync,
		obj_in=camp_instance_coach_in,
	)


	assert camp_instance_coach.camp_instance_id == camp_instance.id
	assert camp_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_get_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await camp_instances_coaches_crud.create(
		db=db,
		obj_in=camp_instance_coach_in,
	)


	camp_instance_coach_2 = await camp_instances_coaches_crud.get(
		db=db,
		camp_instance_id=camp_instance_coach.camp_instance_id,
		coach_id=camp_instance_coach.coach_id,
	)

	assert camp_instance_coach_2
	assert jsonable_encoder(camp_instance_coach) == jsonable_encoder(camp_instance_coach_2)



@pytest.mark.asyncio
async def test_get_sync_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await db.run_sync(
		camp_instances_coaches_crud.create_sync,
		obj_in=camp_instance_coach_in,
	)


	camp_instance_coach_2 = await db.run_sync(
		camp_instances_coaches_crud.get_sync,
		camp_instance_id=camp_instance_coach.camp_instance_id,
		coach_id=camp_instance_coach.coach_id,
	)

	assert camp_instance_coach_2
	assert jsonable_encoder(camp_instance_coach) == jsonable_encoder(camp_instance_coach_2)



@pytest.mark.asyncio
async def test_update_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await camp_instances_coaches_crud.create(
		db=db,
		obj_in=camp_instance_coach_in,
	)

	new_role = 'apple'

	camp_instance_coach_in_update = CampInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	camp_instance_coach_2 = await camp_instances_coaches_crud.update(
		db=db,
		db_obj=camp_instance_coach,
		obj_in=camp_instance_coach_in_update,
	)

	assert camp_instance_coach_2
	assert camp_instance_coach_2.role is not None
	assert camp_instance_coach_2.role == new_role




@pytest.mark.asyncio
async def test_update_sync_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await db.run_sync(
		camp_instances_coaches_crud.create_sync,
		obj_in=camp_instance_coach_in,
	)


	new_role = 'apple'

	camp_instance_coach_in_update = CampInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	camp_instance_coach_2 = await db.run_sync(
		camp_instances_coaches_crud.update_sync,
		db_obj=camp_instance_coach,
		obj_in=camp_instance_coach_in_update,
	)

	assert camp_instance_coach_2
	assert camp_instance_coach_2.role is not None
	assert camp_instance_coach_2.role == new_role




@pytest.mark.asyncio
async def test_delete_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await camp_instances_coaches_crud.create(
		db=db,
		obj_in=camp_instance_coach_in,
	)

	camp_instance_coach_2 = await camp_instances_coaches_crud.delete(
		db=db,
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
	)

	camp_instance_coach_3 = await camp_instances_coaches_crud.get(
		db=db,
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
	)

	assert camp_instance_coach_3 is None
	assert camp_instance_coach_2.camp_instance_id == camp_instance_coach.camp_instance_id
	assert camp_instance_coach_2.coach_id == camp_instance_coach.coach_id



@pytest.mark.asyncio
async def test_delete_sync_camp_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	camp_instance_coach_in = CampInstancesCoachesSchemaCreate(
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	camp_instance_coach = await db.run_sync(
		camp_instances_coaches_crud.create_sync,
		obj_in=camp_instance_coach_in,
	)

	camp_instance_coach_2 = await db.run_sync(
		camp_instances_coaches_crud.delete_sync,
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
	)

	camp_instance_coach_3 = await db.run_sync(
		camp_instances_coaches_crud.get_sync,
		camp_instance_id=camp_instance.id,
		coach_id=coach.id,
	)

	assert camp_instance_coach_3 is None
	assert camp_instance_coach_2.camp_instance_id == camp_instance_coach.camp_instance_id
	assert camp_instance_coach_2.coach_id == camp_instance_coach.coach_id





