from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.player import (
	player_crud,
)

from main.schemas.data.person.player import (
	PlayerSchemaCreate,
	PlayerSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_player(
	db: AsyncSession,
) -> None:
	pass





