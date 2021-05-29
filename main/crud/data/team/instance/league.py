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

from app.models.data.team.instance.league import LeagueInstanceModel

from app.schemas.data.team.instance.league import (
	LeagueInstanceSchemaCreate,
	LeagueInstanceSchemaUpdate,
)




class CRUDLeagueInstance(
	CRUDBase[
		LeagueInstanceModel,
		LeagueInstanceSchemaCreate,
		LeagueInstanceSchemaUpdate,
	]):
	
	pass



league_instance_crud = CRUDLeagueInstance(LeagueInstanceModel)



