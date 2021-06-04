from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.guardians_players import (
	guardians_players_crud,
)

from main.schemas._many.guardians_players import (
	GuardiansPlayersSchemaCreate,
	GuardiansPlayersSchemaUpdate,
)


from main.crud.data.person.guardian import (
	guardian_crud,
)

from main.schemas.data.person.guardian import (
	GuardianSchemaCreate,
	GuardianSchemaUpdate,
)


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
async def test_create_guardian_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_guardian_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_guardian_player(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_guardian_player(
	db: AsyncSession,
) -> None:
	pass





