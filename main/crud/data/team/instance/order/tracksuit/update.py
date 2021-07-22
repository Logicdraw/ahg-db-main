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

from main.models.data.team.instance.order.tracksuit.update import TeamInstanceTracksuitOrderUpdateModel

from main.schemas.data.team.instance.order.tracksuit.update import (
	TeamInstanceTracksuitOrderUpdateSchemaCreate,
	TeamInstanceTracksuitOrderUpdateSchemaUpdate,
)




class CRUDTeamInstanceTracksuitOrderUpdate(
	CRUDBase[
		TeamInstanceTracksuitOrderUpdateModel,
		TeamInstanceTracksuitOrderUpdateSchemaCreate,
		TeamInstanceTracksuitOrderUpdateSchemaUpdate,
	]):
	
	pass



team_instance_tracksuit_order_update_crud = CRUDTeamInstanceTracksuitOrderUpdate(TeamInstanceTracksuitOrderUpdateModel)



