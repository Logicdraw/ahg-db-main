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


import pytest



@pytest.mark.asyncio
async def test_create_program(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_program(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_program(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_program(
	db: AsyncSession,
) -> None:
	pass





