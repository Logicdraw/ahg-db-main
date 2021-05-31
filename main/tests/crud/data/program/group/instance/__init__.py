from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.group.instance import (
	program_group_instance_crud,
)

from main.schemas.data.program.group.instance import (
	ProgramGroupInstanceSchemaCreate,
	ProgramGroupInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_program_group_instance(
	db: AsyncSession,
) -> None:
	pass



def test_get_program_group_instance(
	db: AsyncSession,
) -> None:
	pass



def test_update_program_group_instance(
	db: AsyncSession,
) -> None:
	pass



def test_delete_program_group_instance(
	db: AsyncSession,
) -> None:
	pass





