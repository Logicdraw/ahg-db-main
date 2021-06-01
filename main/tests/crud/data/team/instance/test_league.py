from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.league import (
	league_instance_crud,
)

from main.schemas.data.team.instance.league import (
	LeagueInstanceSchemaCreate,
	LeagueInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_league_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_league_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_league_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_league_instance(
	db: AsyncSession,
) -> None:
	pass





