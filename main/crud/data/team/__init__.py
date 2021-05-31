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

from main.models.data.team import TeamModel

from main.schemas.data.team import (
	TeamSchemaCreate,
	TeamSchemaUpdate,
)




class CRUDTeam(
	CRUDBase[
		TeamModel,
		TeamSchemaCreate,
		TeamSchemaUpdate,
	]):
	
	pass



team_crud = CRUDTeam(TeamModel)



