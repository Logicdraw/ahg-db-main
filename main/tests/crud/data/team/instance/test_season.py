from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.season import (
	season_instance_crud,
)

from main.schemas.data.team.instance.season import (
	SeasonInstanceSchemaCreate,
	SeasonInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_season_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_season_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_season_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_season_instance(
	db: AsyncSession,
) -> None:
	pass





