from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.instance import (
	program_instance_crud,
)

from main.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_create_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass


@pytest.mark.asyncio
async def test_update_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	pass





