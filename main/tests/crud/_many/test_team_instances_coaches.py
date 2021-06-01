from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.team_instances_coaches import (
	team_instances_coaches_crud,
)

from main.schemas._many.team_instances_coaches import (
	TeamInstancesCoachesSchemaCreate,
	TeamInstancesCoachesSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



import pytest



@pytest.mark.asyncio
async def test_create_team_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_team_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_team_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_team_instance_coach(
	db: AsyncSession,
) -> None:
	pass





