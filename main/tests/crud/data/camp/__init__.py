from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp import (
	camp_crud,
)

from main.schemas.data.camp import (
	CampSchemaCreate,
	CampSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_camp(
	db: AsyncSession,
) -> None:
	pass



def test_get_camp(
	db: AsyncSession,
) -> None:
	pass



def test_update_camp(
	db: AsyncSession,
) -> None:
	pass



def test_delete_camp(
	db: AsyncSession,
) -> None:
	pass





