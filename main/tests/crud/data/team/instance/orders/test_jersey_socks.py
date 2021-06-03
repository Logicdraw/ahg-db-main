from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.orders.jersey_socks import (
	team_instance_jersey_socks_order_crud,
)

from main.schemas.data.team.instance.orders.jersey_socks import (
	TeamInstanceJerseySocksOrderSchemaCreate,
	TeamInstanceJerseySocksOrderSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	pass





