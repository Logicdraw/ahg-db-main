from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.meta.gs import (
	gs_meta_crud,
)

from main.schemas.meta.gs import (
	GSMetaSchemaCreate,
	GSMetaSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_gs_meta(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_gs_meta(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_gs_meta(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_gs_meta(
	db: AsyncSession,
) -> None:
	pass



