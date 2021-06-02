from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.league import (
	league_crud,
)

from main.schemas.data.team.league import (
	LeagueSchemaCreate,
	LeagueSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_create_sync_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_sync_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_sync_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_league(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_sync_league(
	db: AsyncSession,
) -> None:
	pass





