from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.division import (
	division_crud,
)

from main.schemas.data.team.division import (
	DivisionSchemaCreate,
	DivisionSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest


@pytest.mark.asyncio
async def test_create_division(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_division(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_division(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_division(
	db: AsyncSession,
) -> None:
	pass





