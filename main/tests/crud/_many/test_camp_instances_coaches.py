from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.camp_instances_coaches import (
	camp_instances_coaches_crud,
)

from main.schemas._many.camp_instances_coaches import (
	CampInstancesCoachesSchemaCreate,
	CampInstancesCoachesSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_camp_instance_coach(
	db: AsyncSession,
) -> None:
	pass



def test_get_camp_instance_coach(
	db: AsyncSession,
) -> None:
	pass



def test_update_camp_instance_coach(
	db: AsyncSession,
) -> None:
	pass



def test_delete_camp_instance_coach(
	db: AsyncSession,
) -> None:
	pass





