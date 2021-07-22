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

from main.models.data.team.instance.order.jersey_socks.update import TeamInstanceJerseySocksOrderUpdateModel

from main.schemas.data.team.instance.order.jersey_socks.update import (
	TeamInstanceJerseySocksOrderUpdateSchemaCreate,
	TeamInstanceJerseySocksOrderUpdateSchemaUpdate,
)




class CRUDTeamInstanceJerseySocksOrderUpdate(
	CRUDBase[
		TeamInstanceJerseySocksOrderUpdateModel,
		TeamInstanceJerseySocksOrderUpdateSchemaCreate,
		TeamInstanceJerseySocksOrderUpdateSchemaUpdate,
	]):
	
	pass



team_instance_jersey_socks_order_update_crud = CRUDTeamInstanceJerseySocksOrderUpdate(TeamInstanceJerseySocksOrderUpdateModel)



