from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form import (
	form_crud,
)

from main.schemas.form import (
	FormSchemaCreate,
	FormSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_form(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_form(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_form(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_form(
	db: AsyncSession,
) -> None:
	pass



