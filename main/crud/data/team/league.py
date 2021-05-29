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

from app.models.data.team.league import LeagueModel

from app.schemas.data.team.league import (
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



