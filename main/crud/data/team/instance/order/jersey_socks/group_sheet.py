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

from main.models.data.team.instance.order.jersey_socks.group_sheet import TeamInstanceJerseySocksOrderGroupSheetModel

from main.schemas.data.team.instance.order.jersey_socks.group_sheet import (
	TeamInstanceJerseySocksOrderGroupSheetSchemaCreate,
	TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate,
)




class CRUDTeamInstanceJerseySocksOrderGroupSheet(
	CRUDBase[
		TeamInstanceJerseySocksOrderGroupSheetModel,
		TeamInstanceJerseySocksOrderGroupSheetSchemaCreate,
		TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate,
	]):
	
	pass



team_instance_jersey_socks_order_group_sheet_crud = CRUDTeamInstanceJerseySocksOrderGroupSheet(TeamInstanceJerseySocksOrderGroupSheetModel)



