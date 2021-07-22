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

from main.models.data.team.instance.orders.tracksuit import TeamInstanceTracksuitOrderModel

from main.schemas.data.team.instance.orders.tracksuit import (
	TeamInstanceTracksuitOrderSchemaCreate,
	TeamInstanceTracksuitOrderSchemaUpdate,
)




class CRUDTeamInstanceTracksuitOrder(
	CRUDBase[
		TeamInstanceTracksuitOrderModel,
		TeamInstanceTracksuitOrderSchemaCreate,
		TeamInstanceTracksuitOrderSchemaUpdate,
	]):
	
	pass



team_instance_tracksuit_order_crud = CRUDTeamInstanceTracksuitOrder(TeamInstanceTracksuitOrderModel)



