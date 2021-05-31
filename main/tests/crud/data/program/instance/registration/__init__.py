from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


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



def test_create_program_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_get_program_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_update_program_instance_registration(
	db: AsyncSession,
) -> None:
	pass



def test_delete_program_instance_registration(
	db: AsyncSession,
) -> None:
	pass





