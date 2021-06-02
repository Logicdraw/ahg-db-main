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


from main.crud.base import CRUDBase

from main.models._many.team_instances_players import TeamInstancesPlayersModel

from main.schemas._many.team_instances_players import (
	TeamInstancesPlayersSchemaCreate,
	TeamInstancesPlayersSchemaUpdate,
)



class CRUDTeamInstancesPlayers(
	CRUDBase[
		TeamInstancesPlayersModel,
		TeamInstancesPlayersSchemaCreate,
		TeamInstancesPlayersSchemaUpdate,
	]):

	async def get(
		self,
		db: AsyncSession,
		team_instance_id: int,
		player_id: int,
	) -> Optional[TeamInstancesPlayersModel]:
		# --

		result = await db.execute(
			select(TeamInstancesPlayersModel).\
			filter_by(
				team_instance_id=team_instance_id,
				player_id=player_id,
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




team_instances_players_crud = CRUDTeamInstancesPlayers(TeamInstancesPlayersModel)



