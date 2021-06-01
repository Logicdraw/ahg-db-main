from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.registration import (
	team_instance_registration_crud,
)

from main.schemas.data.team.instance.registration import (
	TeamInstanceRegistrationSchemaCreate,
	TeamInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_team_instance_registration(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_team_instance_registration(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_team_instance_registration(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_team_instance_registration(
	db: AsyncSession,
) -> None:
	pass





