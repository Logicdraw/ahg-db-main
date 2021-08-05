from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.program_instances_program_instance_registrations import (
	program_instances_program_instance_registrations_crud,
)

from main.schemas._many.program_instances_program_instance_registrations import (
	ProgramInstancesProgramInstanceRegistrationsSchemaCreate,
	ProgramInstancesProgramInstanceRegistrationsSchemaUpdate,
)



from main.crud.data.program.instance import (
	program_instance_crud,
)

from main.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
)



from main.crud.data.program.instance.registration import (
	program_instance_registration_crud,
)

from main.schemas.data.program.instance.registration import (
	ProgramInstanceRegistrationSchemaCreate,
	ProgramInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await program_instances_program_instance_registrations_crud.create(
		db=db,
		obj_in=program_instance_program_instance_registration_in,
	)


	assert program_instance_program_instance_registration.program_instance_id == program_instance.id
	assert program_instance_program_instance_registration.program_instance_registration_id == program_instance_registration.id



@pytest.mark.asyncio
async def test_create_sync_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await db.run_sync(
		program_instances_program_instance_registrations_crud.create_sync,
		obj_in=program_instance_program_instance_registration_in,
	)


	assert program_instance_program_instance_registration.program_instance_id == program_instance.id
	assert program_instance_program_instance_registration.program_instance_registration_id == program_instance_registration.id



@pytest.mark.asyncio
async def test_get_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await program_instances_program_instance_registrations_crud.create(
		db=db,
		obj_in=program_instance_program_instance_registration_in,
	)


	program_instance_program_instance_registration_2 = await program_instances_program_instance_registrations_crud.get(
		db=db,
		program_instance_id=program_instance_program_instance_registration.program_instance_id,
		program_instance_registration_id=program_instance_program_instance_registration.program_instance_registration_id,
	)

	assert program_instance_program_instance_registration_2
	assert jsonable_encoder(program_instance_program_instance_registration) == jsonable_encoder(program_instance_program_instance_registration_2)



@pytest.mark.asyncio
async def test_get_sync_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await db.run_sync(
		program_instances_program_instance_registrations_crud.create_sync,
		obj_in=program_instance_program_instance_registration_in,
	)


	program_instance_program_instance_registration_2 = await db.run_sync(
		program_instances_program_instance_registrations_crud.get_sync,
		program_instance_id=program_instance_program_instance_registration.program_instance_id,
		program_instance_registration_id=program_instance_program_instance_registration.program_instance_registration_id,
	)

	assert program_instance_program_instance_registration_2
	assert jsonable_encoder(program_instance_program_instance_registration) == jsonable_encoder(program_instance_program_instance_registration_2)



@pytest.mark.asyncio
async def test_update_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await program_instances_program_instance_registrations_crud.create(
		db=db,
		obj_in=program_instance_program_instance_registration_in,
	)


	program_instance_program_instance_registration_in_update = ProgramInstancesProgramInstanceRegistrationsSchemaUpdate()

	program_instance_program_instance_registration_2 = await program_instances_program_instance_registrations_crud.update(
		db=db,
		db_obj=program_instance_program_instance_registration,
		obj_in=program_instance_program_instance_registration_in_update,
	)

	assert program_instance_program_instance_registration_2




@pytest.mark.asyncio
async def test_update_sync_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await db.run_sync(
		program_instances_program_instance_registrations_crud.create_sync,
		obj_in=program_instance_program_instance_registration_in,
	)



	program_instance_program_instance_registration_in_update = ProgramInstancesProgramInstanceRegistrationsSchemaUpdate()

	program_instance_program_instance_registration_2 = await db.run_sync(
		program_instances_program_instance_registrations_crud.update_sync,
		db_obj=program_instance_program_instance_registration,
		obj_in=program_instance_program_instance_registration_in_update,
	)

	assert program_instance_program_instance_registration_2




@pytest.mark.asyncio
async def test_delete_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await program_instances_program_instance_registrations_crud.create(
		db=db,
		obj_in=program_instance_program_instance_registration_in,
	)

	program_instance_program_instance_registration_2 = await program_instances_program_instance_registrations_crud.delete(
		db=db,
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration_3 = await program_instances_program_instance_registrations_crud.get(
		db=db,
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	assert program_instance_program_instance_registration_3 is None
	assert program_instance_program_instance_registration_2.program_instance_id == program_instance_program_instance_registration.program_instance_id
	assert program_instance_program_instance_registration_2.program_instance_registration_id == program_instance_program_instance_registration.program_instance_registration_id



@pytest.mark.asyncio
async def test_delete_sync_program_instance_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	program_instance_in = ProgramInstanceSchemaCreate()

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate()

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)


	program_instance_program_instance_registration_in = ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration = await db.run_sync(
		program_instances_program_instance_registrations_crud.create_sync,
		obj_in=program_instance_program_instance_registration_in,
	)

	program_instance_program_instance_registration_2 = await db.run_sync(
		program_instances_program_instance_registrations_crud.delete_sync,
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	program_instance_program_instance_registration_3 = await db.run_sync(
		program_instances_program_instance_registrations_crud.get_sync,
		program_instance_id=program_instance.id,
		program_instance_registration_id=program_instance_registration.id,
	)

	assert program_instance_program_instance_registration_3 is None
	assert program_instance_program_instance_registration_2.program_instance_id == program_instance_program_instance_registration.program_instance_id
	assert program_instance_program_instance_registration_2.program_instance_registration_id == program_instance_program_instance_registration.program_instance_registration_id





