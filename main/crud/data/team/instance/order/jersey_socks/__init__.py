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

from main.models.data.team.instance.order.jersey_socks import TeamInstanceJerseySocksOrderModel

from main.schemas.data.team.instance.order.jersey_socks import (
	TeamInstanceJerseySocksOrderSchemaCreate,
	TeamInstanceJerseySocksOrderSchemaUpdate,
)




class CRUDTeamInstanceJerseySocksOrder(
	CRUDBase[
		TeamInstanceJerseySocksOrderModel,
		TeamInstanceJerseySocksOrderSchemaCreate,
		TeamInstanceJerseySocksOrderSchemaUpdate,
	]):
	
	pass



team_instance_jersey_socks_order_crud = CRUDTeamInstanceJerseySocksOrder(TeamInstanceJerseySocksOrderModel)



