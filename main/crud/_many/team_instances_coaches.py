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

from app.models._many.team_instances_coaches import TeamInstancesCoachesModel

from app.schemas._many.team_instances_coaches import (
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




team_instances_coaches_crud = CRUDTeamInstancesCoaches(TeamInstancesCoachesModel)



