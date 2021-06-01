from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.group import (
	camp_group_crud,
)

from main.schemas.data.camp.group import (
	CampGroupSchemaCreate,
	CampGroupSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_camp_group(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_camp_group(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_camp_group(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_camp_group(
	db: AsyncSession,
) -> None:
	pass





