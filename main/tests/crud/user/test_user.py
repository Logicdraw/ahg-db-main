# Really should be only CRUD (too late haha) !


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.user import user_crud


from main.schemas.user import (
	UserSchemaCreate,
	UserSchemaUpdate,
)


from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_user(
	db: AsyncSession,
) -> None:
	"""
	Create user
	"""

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)


	assert user.email == email
	assert hasattr(user, 'password_hash')



@pytest.mark.asyncio
async def test_create_sync_user(
	db: AsyncSession,
) -> None:
	"""
	Create user
	"""

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await db.run_sync(
		user_crud.create_sync,
		obj_in=user_in,
	)

	assert user.email == email
	assert hasattr(user, 'password_hash')



@pytest.mark.asyncio
async def test_get_user(
	db: AsyncSession,
) -> None:
	# Get User --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	user_2 = await user_crud.get(
		db=db,
		id=user.id,
	)


	assert user_2
	assert jsonable_encoder(user) == jsonable_encoder(user_2)



@pytest.mark.asyncio
async def test_get_sync_user(
	db: AsyncSession,
) -> None:
	# Get User Sync --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await db.run_sync(
		user_crud.create_sync,
		obj_in=user_in,
	)

	user_2 = await db.run_sync(
		user_crud.get_sync,
		id=user.id,
	)


	assert user_2
	assert jsonable_encoder(user) == jsonable_encoder(user_2)



@pytest.mark.asyncio
async def test_update_user(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	new_name = random_name()

	user_in_update = UserSchemaUpdate(
		name=new_name,
	)


	user_2 = await user_crud.update(
		db=db,
		db_obj=user,
		obj_in=user_in_update,
	)

	assert user_2
	assert user_2.name
	assert user_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_user(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await db.run_sync(
		user_crud.create_sync,
		obj_in=user_in,
	)

	new_name = random_name()

	user_in_update = UserSchemaUpdate(
		name=new_name,
	)


	user_2 = await db.run_sync(
		user_crud.update_sync,
		db_obj=user,
		obj_in=user_in_update,
	)

	assert user_2
	assert user_2.name
	assert user_2.name == new_name



@pytest.mark.asyncio
async def test_delete_user(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	user_2 = await user_crud.delete(
		db=db,
		id=user.id,
	)

	user_3 = await user_crud.get(
		db=db,
		id=user.id,
	)


	assert user_3 is None
	assert user_2.id == user.id



@pytest.mark.asyncio
async def test_delete_sync_user(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role=role,
	)

	user = await db.run_sync(
		user_crud.create_sync,
		obj_in=user_in,
	)

	user_2 = await db.run_sync(
		user_crud.delete_sync,
		id=user.id,
	)

	user_3 = await db.run_sync(
		user_crud.get_sync,
		id=user.id,
	)


	assert user_3 is None
	assert user_2.id == user.id



@pytest.mark.asyncio
async def test_check_if_user_is_active(
	db: AsyncSession,
) -> None:
	"""
	User is active
	"""

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		confirm_password=confirm_password,
		name=name,
		role='superadmin',
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_active = user_crud.is_active(user)


	assert is_active is True



@pytest.mark.asyncio
async def test_check_if_user_is_active_inactive(
	db: AsyncSession,
) -> None:
	"""
	Is user active or inactive
	"""

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		is_active=False,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)


	is_active = user_crud.is_active(user)

	assert is_active is False



# Roles --


@pytest.mark.asyncio
async def test_check_if_user_is_superadmin(
	db: AsyncSession,
) -> None:
	# Check if user is superadmin --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_superadmin = user_crud.is_role(
		user=user,
		role='superadmin',
	)

	assert is_superadmin is True



@pytest.mark.asyncio
async def test_check_if_user_is_admin(
	db: AsyncSession,
) -> None:
	# Check if user is admin --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_admin = user_crud.is_role(
		user=user,
		role='admin',
	)

	assert is_admin is True



@pytest.mark.asyncio
async def test_check_if_user_is_coach(
	db: AsyncSession,
) -> None:
	# Check if user is coach --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_coach = user_crud.is_role(
		user=user,
		role='coach',
	)

	assert is_coach is True



@pytest.mark.asyncio
async def test_check_if_user_is_guardian(
	db: AsyncSession,
) -> None:
	# Check if user is guardian --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_guardian = user_crud.is_role(
		user=user,
		role='guardian',
	)

	assert is_guardian is True



@pytest.mark.asyncio
async def test_check_if_user_is_adult_rep(
	db: AsyncSession,
) -> None:
	# Check if user is adult rep --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_adult_rep = user_crud.is_role(
		user=user,
		role='adult_rep',
	)

	assert is_adult_rep is True



@pytest.mark.asyncio
async def test_check_if_user_is_superadmin_as_admin(
	db: AsyncSession,
) -> None:
	# --

	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_superadmin = user_crud.is_role(
		user=user,
		role='superadmin',
	)

	assert is_superadmin is False


@pytest.mark.asyncio
async def test_check_if_user_is_superadmin_as_coach(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_superadmin = user_crud.is_role(
		user=user,
		role='superadmin',
	)

	assert is_superadmin is False


@pytest.mark.asyncio
async def test_check_if_user_is_superadmin_as_guardian(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_superadmin = user_crud.is_role(
		user=user,
		role='superadmin',
	)

	assert is_superadmin is False



@pytest.mark.asyncio
async def test_check_if_user_is_superadmin_as_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_superadmin = user_crud.is_role(
		user=user,
		role='superadmin',
	)

	assert is_superadmin is False



@pytest.mark.asyncio
async def test_check_if_user_is_admin_as_superadmin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_admin = user_crud.is_role(
		user=user,
		role='admin',
	)

	assert is_admin is False


@pytest.mark.asyncio
async def test_check_if_user_is_admin_as_coach(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_admin = user_crud.is_role(
		user=user,
		role='admin',
	)

	assert is_admin is False


@pytest.mark.asyncio
async def test_check_if_user_is_admin_as_guardian(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_admin = user_crud.is_role(
		user=user,
		role='admin',
	)

	assert is_admin is False



@pytest.mark.asyncio
async def test_check_if_user_is_admin_as_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_admin = user_crud.is_role(
		user=user,
		role='admin',
	)

	assert is_admin is False



@pytest.mark.asyncio
async def test_check_if_user_is_coach_as_superadmin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_coach = user_crud.is_role(
		user=user,
		role='coach',
	)

	assert is_coach is False


@pytest.mark.asyncio
async def test_check_if_user_is_coach_as_admin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_coach = user_crud.is_role(
		user=user,
		role='coach',
	)

	assert is_coach is False


@pytest.mark.asyncio
async def test_check_if_user_is_coach_as_guardian(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_coach = user_crud.is_role(
		user=user,
		role='coach',
	)

	assert is_coach is False



@pytest.mark.asyncio
async def test_check_if_user_is_coach_as_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_coach = user_crud.is_role(
		user=user,
		role='coach',
	)

	assert is_coach is False



@pytest.mark.asyncio
async def test_check_if_user_is_guardian_as_superadmin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_guardian = user_crud.is_role(
		user=user,
		role='guardian',
	)

	assert is_guardian is False


@pytest.mark.asyncio
async def test_check_if_user_is_guardian_as_admin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_guardian = user_crud.is_role(
		user=user,
		role='guardian',
	)

	assert is_guardian is False


@pytest.mark.asyncio
async def test_check_if_user_is_guardian_as_coach(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_guardian = user_crud.is_role(
		user=user,
		role='guardian',
	)

	assert is_guardian is False



@pytest.mark.asyncio
async def test_check_if_user_is_guardian_as_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'adult_rep'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_guardian = user_crud.is_role(
		user=user,
		role='guardian',
	)

	assert is_guardian is False




@pytest.mark.asyncio
async def test_check_if_user_is_adult_rep_as_superadmin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_adult_rep = user_crud.is_role(
		user=user,
		role='adult_rep',
	)

	assert is_adult_rep is False


@pytest.mark.asyncio
async def test_check_if_user_is_adult_rep_as_admin(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'admin'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_adult_rep = user_crud.is_role(
		user=user,
		role='adult_rep',
	)

	assert is_adult_rep is False


@pytest.mark.asyncio
async def test_check_if_user_is_adult_rep_as_coach(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'coach'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_adult_rep = user_crud.is_role(
		user=user,
		role='adult_rep',
	)

	assert is_adult_rep is False



@pytest.mark.asyncio
async def test_check_if_user_is_adult_rep_as_guardian(
	db: AsyncSession,
) -> None:
	# --
	email = random_email()
	password = random_lower_string()
	confirm_password = password
	name = random_name()
	role = 'guardian'

	user_in = UserSchemaCreate(
		email=email,
		password=password,
		name=name,
		confirm_password=confirm_password,
		role=role,
	)

	user = await user_crud.create(
		db=db,
		obj_in=user_in,
	)

	is_adult_rep = user_crud.is_role(
		user=user,
		role='adult_rep',
	)

	assert is_adult_rep is False






