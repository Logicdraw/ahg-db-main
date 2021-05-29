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

from app.models.data.team import TeamModel

from app.schemas.data.team import (
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



