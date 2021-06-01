from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.coach import (
	coach_crud,
)

from main.schemas.data.person.coach import (
	CoachSchemaCreate,
	CoachSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_coach(
	db: AsyncSession,
) -> None:
	pass





