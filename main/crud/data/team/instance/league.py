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

from main.models.data.team.instance.league import LeagueInstanceModel

from main.schemas.data.team.instance.league import (
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



