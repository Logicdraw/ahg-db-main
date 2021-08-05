# # SAVE FOR LATER (LAST!!) --


# from fastapi.encoders import jsonable_encoder

# from sqlalchemy.ext.asyncio import AsyncSession


# from main.crud.data.program.instance.registration.invite import (
# 	program_instance_registration_invite_invite_crud,
# )

# from main.schemas.data.program.instance.registration.invite import (
# 	ProgramInstanceRegistrationInviteSchemaCreate,
# 	ProgramInstanceRegistrationInviteSchemaUpdate,
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
# async def test_create_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await program_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	assert program_instance_registration_invite.email_to = email_to



# @pytest.mark.asyncio
# async def test_create_sync_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await db.run_sync(
# 		program_instance_registration_invite_crud.create_sync,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	assert program_instance_registration_invite.email_to = email_to



# @pytest.mark.asyncio
# async def test_get_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await program_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	program_instance_registration_invite_2 = await program_instance_registration_invite_crud.get(
# 		db=db,
# 		id=program_instance_registration_invite.id,
# 	)

# 	assert program_instance_registration_invite_2
# 	assert jsonable_encoder(program_instance_registration_invite_2) == jsonable_encoder(program_instance_registration_invite)


# @pytest.mark.asyncio
# async def test_get_sync_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await db.run_sync(
# 		program_instance_registration_invite_crud.create_sync,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	program_instance_registration_invite_2 = await db.run_sync(
# 		program_instance_registration_invite_crud.get_sync,
# 		id=program_instance_registration_invite.id,
# 	)

# 	assert program_instance_registration_invite_2
# 	assert jsonable_encoder(program_instance_registration_invite_2) == jsonable_encoder(program_instance_registration_invite)




# @pytest.mark.asyncio
# async def test_update_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await program_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=program_instance_registration_invite_in,
# 	)


# 	new_email_to = random_email()
# 	while new_email_to == email_to:
# 		new_email_to = random_email()

# 	program_instance_registration_invite_in_update = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=new_email_to,
# 	)

# 	program_instance_registration_invite_2 = await program_instance_registration_invite_crud.update(
# 		db=db,
# 		db_obj=program_instance_registration_invite,
# 		obj_in=program_instance_registration_invite_in_update,
# 	)

# 	assert program_instance_registration_invite_2
# 	assert program_instance_registration_invite_2.email_to == new_email_to



# @pytest.mark.asyncio
# async def test_update_sync_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await db.run_sync(
# 		program_instance_registration_invite_crud.create_sync,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	new_email_to = random_email()
# 	while new_email_to == email_to:
# 		new_email_to = random_email()

# 	program_instance_registration_invite_in_update = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=new_email_to,
# 	)

# 	program_instance_registration_invite_2 = await db.run_sync(
# 		program_instance_registration_invite_crud.update_sync,
# 		db_obj=program_instance_registration_invite,
# 		obj_in=program_instance_registration_invite_in_update,
# 	)

# 	assert program_instance_registration_invite_2
# 	assert program_instance_registration_invite_2.email_to == new_email_to




# @pytest.mark.asyncio
# async def test_delete_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await program_instance_registration_invite_crud.create(
# 		db=db,
# 		obj_in=program_instance_registration_invite_in,
# 	)

# 	program_instance_registration_invite_2 = await program_instance_registration_invite_crud.delete(
# 		db=db,
# 		id=program_instance_registration_invite.id,
# 	)

# 	program_instance_registration_invite_3 = await program_instance_registration_invite_crud.get(
# 		db=db,
# 		id=program_instance_registration_invite.id,
# 	)


# 	assert program_instance_registration_invite_3 is None
# 	assert program_instance_registration_invite_2.id == program_instance_registration_invite.id



# @pytest.mark.asyncio
# async def test_delete_sync_program_instance_registration_invite(
# 	db: AsyncSession,
# ) -> None:
# 	# --

# 	email_to = random_email()
# 	has_registered = False

# 	program_instance_registration_invite_in = ProgramInstanceRegistrationInviteSchemaCreate(
# 		email_to=email_to,
# 		has_registered=has_registered,
# 	)

# 	program_instance_registration_invite = await db.run_sync(
# 		program_instance_registration_invite_crud.create_sync,
# 		obj_in=program_instance_registration_invite_in,
# 	)


# 	program_instance_registration_invite_2 = await db.run_sync(
# 		program_instance_registration_invite_crud.delete_sync,
# 		id=program_instance_registration_invite.id,
# 	)

# 	program_instance_registration_invite_3 = await db.run_sync(
# 		program_instance_registration_invite_crud.get_sync,
# 		id=program_instance_registration_invite.id,
# 	)


# 	assert program_instance_registration_invite_3 is None
# 	assert program_instance_registration_invite_2.id == program_instance_registration_invite.id





