from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.meta.spng import (
	spng_meta_crud,
)

from main.schemas.meta.spng import (
	SpngMetaSchemaCreate,
	SpngMetaSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_spng_meta(
	db: AsyncSession,
) -> None:
	pass



def test_get_spng_meta(
	db: AsyncSession,
) -> None:
	pass



def test_update_spng_meta(
	db: AsyncSession,
) -> None:
	pass



def test_delete_spng_meta(
	db: AsyncSession,
) -> None:
	pass



