from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form import (
	form_crud,
)

from main.schemas.form import (
	FormSchemaCreate,
	FormSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_form(
	db: AsyncSession,
) -> None:
	pass



def test_get_form(
	db: AsyncSession,
) -> None:
	pass



def test_update_form(
	db: AsyncSession,
) -> None:
	pass



def test_delete_form(
	db: AsyncSession,
) -> None:
	pass



