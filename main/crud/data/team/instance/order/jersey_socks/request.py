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

from main.models.data.team.instance.order.jersey_socks.request import TeamInstanceJerseySocksOrderRequestModel

from main.schemas.data.team.instance.order.jersey_socks.request import (
	TeamInstanceJerseySocksOrderRequestSchemaCreate,
	TeamInstanceJerseySocksOrderRequestSchemaUpdate,
)




class CRUDTeamInstanceJerseySocksOrderRequest(
	CRUDBase[
		TeamInstanceJerseySocksOrderRequestModel,
		TeamInstanceJerseySocksOrderRequestSchemaCreate,
		TeamInstanceJerseySocksOrderRequestSchemaUpdate,
	]):
	
	pass



team_instance_jersey_socks_order_request_crud = CRUDTeamInstanceJerseySocksOrderRequest(TeamInstanceJerseySocksOrderRequestModel)



