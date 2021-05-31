from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.division import (
	division_instance_crud,
)

from main.schemas.data.team.instance.division import (
	DivisionInstanceSchemaCreate,
	DivisionInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_division_instance(
	db: AsyncSession,
) -> None:
	pass



def test_get_division_instance(
	db: AsyncSession,
) -> None:
	pass



def test_update_division_instance(
	db: AsyncSession,
) -> None:
	pass



def test_delete_division_instance(
	db: AsyncSession,
) -> None:
	pass





