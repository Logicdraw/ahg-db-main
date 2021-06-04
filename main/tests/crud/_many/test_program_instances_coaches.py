from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.program_instances_coaches import (
	program_instances_coaches_crud,
)

from main.schemas._many.program_instances_coaches import (
	ProgramInstancesCoachesSchemaCreate,
	ProgramInstancesCoachesSchemaUpdate,
)


from main.crud.data.program.instance import (
	program_instance_crud,
)

from main.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
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
async def test_create_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await program_instances_coaches_crud.create(
		db=db,
		obj_in=program_instance_coach_in,
	)


	assert program_instance_coach.program_instance_id == program_instance.id
	assert program_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_create_sync_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await db.run_sync(
		program_instances_coaches_crud.create_sync,
		obj_in=program_instance_coach_in,
	)


	assert program_instance_coach.program_instance_id == program_instance.id
	assert program_instance_coach.coach_id == coach.id



@pytest.mark.asyncio
async def test_get_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await program_instances_coaches_crud.create(
		db=db,
		obj_in=program_instance_coach_in,
	)

	program_instance_coach_2 = await program_instances_coaches_crud.get(
		db=db,
		program_instance_id=program_instance_coach.program_instance_id,
		coach_id=program_instance_coach.coach_instance_id,
	)

	assert program_instance_coach_2
	assert jsonable_encoder(program_instance_coach) == jsonable_encoder(program_instance_coach_2)



@pytest.mark.asyncio
async def test_get_sync_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await db.run_sync(
		program_instances_coaches_crud.create_sync,
		obj_in=program_instance_coach_in,
	)


	program_instance_coach_2 = await db.run_sync(
		program_instances_coaches_crud.get_sync,
		program_instance_id=program_instance_coach.program_instance_id,
		coach_id=program_instance_coach.coach_instance_id,
	)

	assert program_instance_coach_2
	assert jsonable_encoder(program_instance_coach) == jsonable_encoder(program_instance_coach_2)




@pytest.mark.asyncio
async def test_update_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await program_instances_coaches_crud.create(
		db=db,
		obj_in=program_instance_coach_in,
	)


	new_role = 'apple'

	program_instance_coach_in_update = ProgramInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	program_instance_coach_2 = await program_instances_coaches_crud.update(
		db=db,
		obj_in=program_instance_coach_in_update,
	)

	assert program_instance_coach_2
	assert program_instance_coach_2.role
	assert program_instance_coach_2.role == new_role



@pytest.mark.asyncio
async def test_update_sync_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await db.run_sync(
		program_instances_coaches_crud.create_sync,
		obj_in=program_instance_coach_in,
	)


	new_role = 'apple'

	program_instance_coach_in_update = ProgramInstancesCoachesSchemaUpdate(
		role=new_role,
	)

	program_instance_coach_2 = await db.run_sync(
		program_instances_coaches_crud.update_sync,
		obj_in=program_instance_coach_in_update,
	)

	assert program_instance_coach_2
	assert program_instance_coach_2.role
	assert program_instance_coach_2.role == new_role



@pytest.mark.asyncio
async def test_delete_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await program_instances_coaches_crud.create(
		db=db,
		obj_in=program_instance_coach_in,
	)

	program_instance_coach_2 = await program_instances_coaches_crud.delete(
		db=db,
		program_instance_id=program_instance.id,
		coach_id=coach.id,
	)

	program_instance_coach_3 = await program_instances_coaches_crud.get(
		db=db,
		program_instance_id=program_instance.id,
		coach_id=coach.id,
	)

	assert program_instance_coach_3 is None
	assert program_instance_coach_2.program_instance_id == program_instance_coach.camp_instance_id
	assert program_instance_coach_2.coach_id == program_instance_coach.coach_id




@pytest.mark.asyncio
async def test_delete_sync_program_instance_coach(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	coach_in = CoachSchemaCreate()

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	program_instance_coach_in = ProgramInstancesCoachesSchemaCreate(
		program_instance_id=program_instance.id,
		coach_id=coach.id,
		role='banana',
	)

	program_instance_coach = await db.run_sync(
		program_instances_coaches_crud.create_sync,
		obj_in=program_instance_coach_in,
	)


	program_instance_coach_2 = await db.run_sync(
		program_instances_coaches_crud.delete_sync,
		program_instance_id=program_instance.id,
		coach_id=coach.id,
	)

	program_instance_coach_3 = await db.run_sync(
		program_instances_coaches_crud.get_sync,
		program_instance_id=program_instance.id,
		coach_id=coach.id,
	)

	assert program_instance_coach_3 is None
	assert program_instance_coach_2.program_instance_id == program_instance_coach.camp_instance_id
	assert program_instance_coach_2.coach_id == program_instance_coach.coach_id






