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

from main.models.data.team.instance.order.tracksuit.request import TeamInstanceTracksuitOrderRequestModel

from main.schemas.data.team.instance.order.tracksuit.request import (
	TeamInstanceTracksuitOrderRequestSchemaCreate,
	TeamInstanceTracksuitOrderRequestSchemaUpdate,
)




class CRUDTeamInstanceTracksuitOrderRequest(
	CRUDBase[
		TeamInstanceTracksuitOrderRequestModel,
		TeamInstanceTracksuitOrderRequestSchemaCreate,
		TeamInstanceTracksuitOrderRequestSchemaUpdate,
	]):
	
	pass



team_instance_tracksuit_order_request_crud = CRUDTeamInstanceTracksuitOrderRequest(TeamInstanceTracksuitOrderRequestModel)



