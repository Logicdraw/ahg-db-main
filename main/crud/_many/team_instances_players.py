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

from app.models._many.team_instances_players import TeamInstancesPlayersModel

from app.schemas._many.team_instances_players import (
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




team_instances_players_crud = CRUDTeamInstancesPlayers(TeamInstancesPlayersModel)



