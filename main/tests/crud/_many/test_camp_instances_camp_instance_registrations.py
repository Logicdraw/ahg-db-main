from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.camp_instances_camp_instance_registrations import (
	camp_instances_camp_instance_registrations_crud,
)

from main.schemas._many.camp_instances_camp_instance_registrations import (
	CampInstancesCampInstanceRegistrationsSchemaCreate,
	CampInstancesCampInstanceRegistrationsSchemaUpdate,
)



from main.crud.data.camp.instance import (
	camp_instance_crud,
)

from main.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
)



from main.crud.data.camp.instance.registration import (
	camp_instance_registration_crud,
)

from main.schemas.data.camp.instance.registration import (
	CampInstanceRegistrationSchemaCreate,
	CampInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await camp_instances_camp_instance_registrations_crud.create(
		db=db,
		obj_in=camp_instance_camp_instance_registration_in,
	)


	assert camp_instance_camp_instance_registration.camp_instance_id == camp_instance.id
	assert camp_instance_camp_instance_registration.camp_instance_registration_id == camp_instance_registration.id



@pytest.mark.asyncio
async def test_create_sync_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.create_sync,
		obj_in=camp_instance_camp_instance_registration_in,
	)


	assert camp_instance_camp_instance_registration.camp_instance_id == camp_instance.id
	assert camp_instance_camp_instance_registration.camp_instance_registration_id == camp_instance_registration.id



@pytest.mark.asyncio
async def test_get_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await camp_instances_camp_instance_registrations_crud.create(
		db=db,
		obj_in=camp_instance_camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_2 = await camp_instances_camp_instance_registrations_crud.get(
		db=db,
		camp_instance_id=camp_instance_camp_instance_registration.camp_instance_id,
		camp_instance_registration_id=camp_instance_camp_instance_registration.camp_instance_registration_id,
	)

	assert camp_instance_camp_instance_registration_2
	assert jsonable_encoder(camp_instance_camp_instance_registration) == jsonable_encoder(camp_instance_camp_instance_registration_2)



@pytest.mark.asyncio
async def test_get_sync_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.create_sync,
		obj_in=camp_instance_camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_2 = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.get_sync,
		camp_instance_id=camp_instance_camp_instance_registration.camp_instance_id,
		camp_instance_registration_id=camp_instance_camp_instance_registration.camp_instance_registration_id,
	)

	assert camp_instance_camp_instance_registration_2
	assert jsonable_encoder(camp_instance_camp_instance_registration) == jsonable_encoder(camp_instance_camp_instance_registration_2)



@pytest.mark.asyncio
async def test_update_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await camp_instances_camp_instance_registrations_crud.create(
		db=db,
		obj_in=camp_instance_camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in_update = CampInstancesCampInstanceRegistrationsSchemaUpdate()

	camp_instance_camp_instance_registration_2 = await camp_instances_camp_instance_registrations_crud.update(
		db=db,
		db_obj=camp_instance_camp_instance_registration,
		obj_in=camp_instance_camp_instance_registration_in_update,
	)

	assert camp_instance_camp_instance_registration_2




@pytest.mark.asyncio
async def test_update_sync_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.create_sync,
		obj_in=camp_instance_camp_instance_registration_in,
	)



	camp_instance_camp_instance_registration_in_update = CampInstancesCampInstanceRegistrationsSchemaUpdate()

	camp_instance_camp_instance_registration_2 = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.update_sync,
		db_obj=camp_instance_camp_instance_registration,
		obj_in=camp_instance_camp_instance_registration_in_update,
	)

	assert camp_instance_camp_instance_registration_2




@pytest.mark.asyncio
async def test_delete_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await camp_instance_crud.create(
		db=db,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await camp_instances_camp_instance_registrations_crud.create(
		db=db,
		obj_in=camp_instance_camp_instance_registration_in,
	)

	camp_instance_camp_instance_registration_2 = await camp_instances_camp_instance_registrations_crud.delete(
		db=db,
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration_3 = await camp_instances_camp_instance_registrations_crud.get(
		db=db,
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	assert camp_instance_camp_instance_registration_3 is None
	assert camp_instance_camp_instance_registration_2.camp_instance_id == camp_instance_camp_instance_registration.camp_instance_id
	assert camp_instance_camp_instance_registration_2.camp_instance_registration_id == camp_instance_camp_instance_registration.camp_instance_registration_id



@pytest.mark.asyncio
async def test_delete_sync_camp_instance_camp_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	camp_instance_in = CampInstanceSchemaCreate()

	camp_instance = await db.run_sync(
		camp_instance_crud.create_sync,
		obj_in=camp_instance_in,
	)


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate()

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_camp_instance_registration_in = CampInstancesCampInstanceRegistrationsSchemaCreate(
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.create_sync,
		obj_in=camp_instance_camp_instance_registration_in,
	)

	camp_instance_camp_instance_registration_2 = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.delete_sync,
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	camp_instance_camp_instance_registration_3 = await db.run_sync(
		camp_instances_camp_instance_registrations_crud.get_sync,
		camp_instance_id=camp_instance.id,
		camp_instance_registration_id=camp_instance_registration.id,
	)

	assert camp_instance_camp_instance_registration_3 is None
	assert camp_instance_camp_instance_registration_2.camp_instance_id == camp_instance_camp_instance_registration.camp_instance_id
	assert camp_instance_camp_instance_registration_2.camp_instance_registration_id == camp_instance_camp_instance_registration.camp_instance_registration_id





