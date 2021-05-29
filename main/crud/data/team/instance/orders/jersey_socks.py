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

from app.models.data.team.instance.orders.jersey_socks import TeamInstanceJerseySocksOrderModel

from app.schemas.data.team.instance.orders.jersey_socks import (
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



