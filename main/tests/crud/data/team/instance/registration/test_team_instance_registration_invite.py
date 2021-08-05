# SAVE FOR LATER (LAST!!) --


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.registration.invite import (
	team_instance_registration_invite_crud,
)

from main.schemas.data.team.instance.registration.invite import (
	TeamInstanceRegistrationInviteSchemaCreate,
	TeamInstanceRegistrationInviteSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest

import datetime

import pytz



@pytest.mark.asyncio
async def test_create_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await team_instance_registration_invite_crud.create(
		db=db,
		obj_in=team_instance_registration_invite_in,
	)

	assert team_instance_registration_invite.email_to == email_to



@pytest.mark.asyncio
async def test_create_sync_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await db.run_sync(
		team_instance_registration_invite_crud.create_sync,
		obj_in=team_instance_registration_invite_in,
	)

	assert team_instance_registration_invite.email_to == email_to



@pytest.mark.asyncio
async def test_get_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await team_instance_registration_invite_crud.create(
		db=db,
		obj_in=team_instance_registration_invite_in,
	)

	team_instance_registration_invite_2 = await team_instance_registration_invite_crud.get(
		db=db,
		id=team_instance_registration_invite.id,
	)

	assert team_instance_registration_invite_2
	assert jsonable_encoder(team_instance_registration_invite_2) == jsonable_encoder(team_instance_registration_invite)


@pytest.mark.asyncio
async def test_get_sync_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await db.run_sync(
		team_instance_registration_invite_crud.create_sync,
		obj_in=team_instance_registration_invite_in,
	)

	team_instance_registration_invite_2 = await db.run_sync(
		team_instance_registration_invite_crud.get_sync,
		id=team_instance_registration_invite.id,
	)

	assert team_instance_registration_invite_2
	assert jsonable_encoder(team_instance_registration_invite_2) == jsonable_encoder(team_instance_registration_invite)




@pytest.mark.asyncio
async def test_update_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await team_instance_registration_invite_crud.create(
		db=db,
		obj_in=team_instance_registration_invite_in,
	)


	new_email_to = random_email()
	while new_email_to == email_to:
		new_email_to = random_email()

	team_instance_registration_invite_in_update = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=new_email_to,
	)

	team_instance_registration_invite_2 = await team_instance_registration_invite_crud.update(
		db=db,
		db_obj=team_instance_registration_invite,
		obj_in=team_instance_registration_invite_in_update,
	)

	assert team_instance_registration_invite_2
	assert team_instance_registration_invite_2.email_to == new_email_to



@pytest.mark.asyncio
async def test_update_sync_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await db.run_sync(
		team_instance_registration_invite_crud.create_sync,
		obj_in=team_instance_registration_invite_in,
	)

	new_email_to = random_email()
	while new_email_to == email_to:
		new_email_to = random_email()

	team_instance_registration_invite_in_update = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=new_email_to,
	)

	team_instance_registration_invite_2 = await db.run_sync(
		team_instance_registration_invite_crud.update_sync,
		db_obj=team_instance_registration_invite,
		obj_in=team_instance_registration_invite_in_update,
	)

	assert team_instance_registration_invite_2
	assert team_instance_registration_invite_2.email_to == new_email_to




@pytest.mark.asyncio
async def test_delete_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await team_instance_registration_invite_crud.create(
		db=db,
		obj_in=team_instance_registration_invite_in,
	)

	team_instance_registration_invite_2 = await team_instance_registration_invite_crud.delete(
		db=db,
		id=team_instance_registration_invite.id,
	)

	team_instance_registration_invite_3 = await team_instance_registration_invite_crud.get(
		db=db,
		id=team_instance_registration_invite.id,
	)


	assert team_instance_registration_invite_3 is None
	assert team_instance_registration_invite_2.id == team_instance_registration_invite.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_registration_invite(
	db: AsyncSession,
) -> None:
	# --

	email_to = random_email()
	has_registered = False

	team_instance_registration_invite_in = TeamInstanceRegistrationInviteSchemaCreate(
		email_to=email_to,
		has_registered=has_registered,
	)

	team_instance_registration_invite = await db.run_sync(
		team_instance_registration_invite_crud.create_sync,
		obj_in=team_instance_registration_invite_in,
	)


	team_instance_registration_invite_2 = await db.run_sync(
		team_instance_registration_invite_crud.delete_sync,
		id=team_instance_registration_invite.id,
	)

	team_instance_registration_invite_3 = await db.run_sync(
		team_instance_registration_invite_crud.get_sync,
		id=team_instance_registration_invite.id,
	)


	assert team_instance_registration_invite_3 is None
	assert team_instance_registration_invite_2.id == team_instance_registration_invite.id





