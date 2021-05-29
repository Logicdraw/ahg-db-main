from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy import (
	func,
	or_,
)


from app.crud.base import CRUDBase

from app.models._many.camp_instances_coaches import CampInstancesCoachesModel

from app.schemas._many.camp_instances_coaches import (
	CampInstancesCoachesSchemaCreate,
	CampInstancesCoachesSchemaUpdate,
)



class CRUDCampInstancesCoaches(
	CRUDBase[
		CampInstancesCoachesModel,
		CampInstancesCoachesSchemaCreate,
		CampInstancesCoachesSchemaUpdate,
	]):

	async def get(
		self,
		db: AsyncSession,
		camp_instance_id: int,
		coach_id: int,
	) -> Optional[CampInstancesCoachesModel]:
		# --

		result = await db.execute(
			select(CampInstancesCoachesModel).\
			filter_by(
				camp_instance_id=camp_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()




camp_instances_coaches_crud = CRUDCampInstancesCoaches(CampInstancesCoachesModel)



