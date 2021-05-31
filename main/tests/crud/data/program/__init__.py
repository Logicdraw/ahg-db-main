from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program import (
	program_crud,
)

from main.schemas.data.program import (
	ProgramSchemaCreate,
	ProgramSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_program(
	db: AsyncSession,
) -> None:
	pass



def test_get_program(
	db: AsyncSession,
) -> None:
	pass



def test_update_program(
	db: AsyncSession,
) -> None:
	pass



def test_delete_program(
	db: AsyncSession,
) -> None:
	pass





