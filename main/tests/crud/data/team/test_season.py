from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.season import (
	season_crud,
)

from main.schemas.data.team.season import (
	SeasonSchemaCreate,
	SeasonSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_create_sync_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_sync_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_sync_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_season(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_sync_season(
	db: AsyncSession,
) -> None:
	pass





