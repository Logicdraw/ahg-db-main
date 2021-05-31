from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


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



def test_create_camp_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_get_camp_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_update_camp_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_delete_camp_instance_registration(
	db: AsyncSession,
) -> None:
	pass





