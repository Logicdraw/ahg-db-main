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




team_instances_players_crud = CRUDTeamInstancesPlayers(TeamInstancesPlayersModel)



