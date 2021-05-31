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



def test_create_league(
	db: AsyncSession,
) -> None:
	pass



def test_get_league(
	db: AsyncSession,
) -> None:
	pass



def test_update_league(
	db: AsyncSession,
) -> None:
	pass



def test_delete_league(
	db: AsyncSession,
) -> None:
	pass





