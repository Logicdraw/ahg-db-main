from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.program_instances_coaches import (
	program_instances_coaches_crud,
)

from main.schemas._many.program_instances_coaches import (
	ProgramInstancesCoachesSchemaCreate,
	ProgramInstancesCoachesSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_program_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_program_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_program_instance_coach(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_program_instance_coach(
	db: AsyncSession,
) -> None:
	pass





