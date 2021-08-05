# # SAVE FOR LATER (LAST!!) --


# from fastapi.encoders import jsonable_encoder

# from sqlalchemy.ext.asyncio import AsyncSession


# from main.crud.data.camp.instance.registration.invite import (
# 	camp_instance_registration_invite_invite_crud,
# )

# from main.schemas.data.camp.instance.registration.invite import (
# 	CampInstanceRegistrationInviteSchemaCreate,
# 	CampInstanceRegistrationInviteSchemaUpdate,
# )



# from main.tests.utils import (
# 	random_email,
# 	random_lower_string,
# 	random_name,
# 	random_number,
# )


# import pytest

# import datetime

# import pytz



# @pytest.mark.asyncio
# async def test_create_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await camp_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	assert camp_instance_registration_invite.email_to = email_to



# @pytest.mark.asyncio
# async def test_create_sync_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await db.run_sync(
# 		camp_instance_registration_invite_crud.create_sync,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	assert camp_instance_registration_invite.email_to = email_to



# @pytest.mark.asyncio
# async def test_get_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await camp_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	camp_instance_registration_invite_2 = await camp_instance_registration_invite_crud.get(
# 		db=db,
# 		id=camp_instance_registration_invite.id,
# 	)

# 	assert camp_instance_registration_invite_2
# 	assert jsonable_encoder(camp_instance_registration_invite_2) == jsonable_encoder(camp_instance_registration_invite)


# @pytest.mark.asyncio
# async def test_get_sync_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await db.run_sync(
# 		camp_instance_registration_invite_crud.create_sync,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	camp_instance_registration_invite_2 = await db.run_sync(
# 		camp_instance_registration_invite_crud.get_sync,
# 		id=camp_instance_registration_invite.id,
# 	)

# 	assert camp_instance_registration_invite_2
# 	assert jsonable_encoder(camp_instance_registration_invite_2) == jsonable_encoder(camp_instance_registration_invite)




# @pytest.mark.asyncio
# async def test_update_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await camp_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=camp_instance_registration_invite_in,
# 	)


# 	new_email_to = random_email()
# 	while new_email_to == email_to:
# 		new_email_to = random_email()

# 	camp_instance_registration_invite_in_update = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=new_email_to,
# 	)

# 	camp_instance_registration_invite_2 = await camp_instance_registration_invite_crud.update(
# 		db=db,
# 		db_obj=camp_instance_registration_invite,
# 		obj_in=camp_instance_registration_invite_in_update,
# 	)

# 	assert camp_instance_registration_invite_2
# 	assert camp_instance_registration_invite_2.email_to == new_email_to



# @pytest.mark.asyncio
# async def test_update_sync_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await db.run_sync(
# 		camp_instance_registration_invite_crud.create_sync,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	new_email_to = random_email()
# 	while new_email_to == email_to:
# 		new_email_to = random_email()

# 	camp_instance_registration_invite_in_update = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=new_email_to,
# 	)

# 	camp_instance_registration_invite_2 = await db.run_sync(
# 		camp_instance_registration_invite_crud.update_sync,
# 		db_obj=camp_instance_registration_invite,
# 		obj_in=camp_instance_registration_invite_in_update,
# 	)

# 	assert camp_instance_registration_invite_2
# 	assert camp_instance_registration_invite_2.email_to == new_email_to




# @pytest.mark.asyncio
# async def test_delete_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await camp_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=camp_instance_registration_invite_in,
# 	)

# 	camp_instance_registration_invite_2 = await camp_instance_registration_invite_crud.delete(
# 		db=db,
# 		id=camp_instance_registration_invite.id,
# 	)

# 	camp_instance_registration_invite_3 = await camp_instance_registration_invite_crud.get(
# 		db=db,
# 		id=camp_instance_registration_invite.id,
# 	)


# 	assert camp_instance_registration_invite_3 is None
# 	assert camp_instance_registration_invite_2.id == camp_instance_registration_invite.id



# @pytest.mark.asyncio
# async def test_delete_sync_camp_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	camp_instance_registration_invite_in = CampInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	camp_instance_registration_invite = await db.run_sync(
# 		camp_instance_registration_invite_crud.create_sync,
# 		obj_in=camp_instance_registration_invite_in,
# 	)


# 	camp_instance_registration_invite_2 = await db.run_sync(
# 		camp_instance_registration_invite_crud.delete_sync,
# 		id=camp_instance_registration_invite.id,
# 	)

# 	camp_instance_registration_invite_3 = await db.run_sync(
# 		camp_instance_registration_invite_crud.get_sync,
# 		id=camp_instance_registration_invite.id,
# 	)


# 	assert camp_instance_registration_invite_3 is None
# 	assert camp_instance_registration_invite_2.id == camp_instance_registration_invite.id





