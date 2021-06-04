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

from main.models._many.team_instances_coaches import TeamInstancesCoachesModel

from main.schemas._many.team_instances_coaches import (
	TeamInstancesCoachesSchemaCreate,
	TeamInstancesCoachesSchemaUpdate,
)



class CRUDTeamInstancesCoaches(
	CRUDBase[
		TeamInstancesCoachesModel,
		TeamInstancesCoachesSchemaCreate,
		TeamInstancesCoachesSchemaUpdate,
	]):

	async def get(
		self,
		db: AsyncSession,
		team_instance_id: int,
		coach_id: int,
	) -> Optional[TeamInstancesCoachesModel]:
		# --

		result = await db.execute(
			select(TeamInstancesCoachesModel).\
			filter_by(
				team_instance_id=team_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()


	def get_sync(
		self,
		db: AsyncSession,
		team_instance_id: int,
		coach_id: int,
	) -> Optional[TeamInstancesCoachesModel]:
		# --

		result = db.execute(
			select(TeamInstancesCoachesModel).\
			filter_by(
				team_instance_id=team_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()




team_instances_coaches_crud = CRUDTeamInstancesCoaches(TeamInstancesCoachesModel)



