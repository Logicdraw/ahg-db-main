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

from main.models.data.team.league import LeagueModel

from main.schemas.data.team.league import (
	LeagueSchemaCreate,
	LeagueSchemaUpdate,
)




class CRUDLeague(
	CRUDBase[
		LeagueModel,
		LeagueSchemaCreate,
		LeagueSchemaUpdate,
	]):
	
	pass



league_crud = CRUDLeague(LeagueModel)



