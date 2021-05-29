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

from app.models.data.team.instance import TeamInstanceModel

from app.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)




class CRUDTeamInstance(
	CRUDBase[
		TeamInstanceModel,
		TeamInstanceSchemaCreate,
		TeamInstanceSchemaUpdate,
	]):
	
	pass



team_instance_crud = CRUDTeamInstance(TeamInstanceModel)



