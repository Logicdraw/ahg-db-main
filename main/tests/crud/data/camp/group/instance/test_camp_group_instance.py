from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.group.instance import (
	camp_group_instance_crud,
)

from main.schemas.data.camp.group.instance import (
	CampGroupInstanceSchemaCreate,
	CampGroupInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_camp_group_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_camp_group_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_camp_group_instance(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_camp_group_instance(
	db: AsyncSession,
) -> None:
	pass





