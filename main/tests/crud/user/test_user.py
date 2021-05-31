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



@pytest.mark.asyncio()
async def test_create_user(
	db: AsyncSession,
) -> None:
	"""
	Create user
	"""

	email = random_email()
	password = random_lower_string()
	name = random_name()
	role = 'superadmin'

	user_in = UserSchemaCreate(email=email, password=password, name=name)
	user = await user_crud.create(db=db, obj_in=user_in)


	assert user.email == email
	assert hasattr(user, 'password_hash')



def test_get_user(
	db: AsyncSession,
) -> None:
	# Get User --

	pass



def test_update_user(
	db: AsyncSession,
) -> None:
	pass



def test_delete_user(
	db: AsyncSession,
) -> None:
	pass




def test_check_if_user_is_active(
	db: AsyncSession,
) -> None:
	"""
	User is active
	"""

	email = random_email()
	password = random_lower_string()
	name = random_name()

	user_in = UserSchemaCreate(email=email, password=password, name=name, role='superuser')
	user = user_crud.create(db=db, obj_in=user_in)

	is_active = user_crud.is_active(user)


	assert is_active is True



def test_check_if_user_is_active_inactive(
	db: AsyncSession,
) -> None:
	"""
	Is user active or inactive
	"""

	email = random_email()
	password = random_lower_string()
	name = random_name()

	user_in = UserSchemaCreate(email=email, password=password, name=name, is_active=False)
	user = user_crud.create(db=db, obj_in=user_in)


	is_active = user_crud.is_active(user)

	assert is_active



# Roles --


def test_check_if_user_is_superadmin(
	db: AsyncSession,
) -> None:
	# Check if user is superadmin --

	pass


def test_check_if_user_is_admin(
	db: AsyncSession,
) -> None:
	# Check if user is admin --

	pass



def test_check_if_user_is_coach(
	db: AsyncSession,
) -> None:

	pass



def test_check_if_user_is_guardian(
	db: AsyncSession,
) -> None:
	pass




def test_check_if_user_is_superadmin_as_admin(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_superadmin_as_coach(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_superadmin_as_guardian(
	db: AsyncSession,
) -> None:
	pass




def test_check_if_user_is_admin_as_superadmin(
	db: AsyncSession,
) -> None:
	pass


def test_check_fi_user_is_admin_as_coach(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_admin_as_guardian(
	db: AsyncSession,
) -> None:
	pass




def test_check_if_user_is_coach_as_superadmin(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_coach_as_admin(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_coach_as_guardian(
	db: AsyncSession,
) -> None:
	pass




def test_check_if_user_is_guardian_as_superadmin(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_guardian_as_admin(
	db: AsyncSession,
) -> None:
	pass


def test_check_if_user_is_guardian_as_coach(
	db: AsyncSession,
) -> None:
	pass







