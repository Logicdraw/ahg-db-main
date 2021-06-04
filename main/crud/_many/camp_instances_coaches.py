from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession



from main.crud.base import CRUDBase

from main.models._many.camp_instances_coaches import CampInstancesCoachesModel

from main.schemas._many.camp_instances_coaches import (
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


	def get_sync(
		self,
		db: AsyncSession,
		camp_instance_id: int,
		coach_id: int,
	) -> Optional[CampInstancesCoachesModel]:
		# --

		result = db.execute(
			select(CampInstancesCoachesModel).\
			filter_by(
				camp_instance_id=camp_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()




camp_instances_coaches_crud = CRUDCampInstancesCoaches(CampInstancesCoachesModel)



