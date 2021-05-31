from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.conference import (
	conference_crud,
)

from main.schemas.data.team.conference import (
	ConferenceSchemaCreate,
	ConferenceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_conference(
	db: AsyncSession,
) -> None:
	pass



def test_get_conference(
	db: AsyncSession,
) -> None:
	pass



def test_update_conference(
	db: AsyncSession,
) -> None:
	pass



def test_delete_conference(
	db: AsyncSession,
) -> None:
	pass





