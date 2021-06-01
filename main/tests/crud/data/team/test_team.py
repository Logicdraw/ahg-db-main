from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team import (
	team_crud,
)

from main.schemas.data.team import (
	TeamSchemaCreate,
	TeamSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_team(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_team(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_team(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_team(
	db: AsyncSession,
) -> None:
	pass





