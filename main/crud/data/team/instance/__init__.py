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

from main.models.data.team.instance import TeamInstanceModel

from main.schemas.data.team.instance import (
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



