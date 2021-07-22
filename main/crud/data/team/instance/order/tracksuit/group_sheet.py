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

from main.models.data.team.instance.order.tracksuit.group_sheet import TeamInstanceTracksuitOrderGroupSheetModel

from main.schemas.data.team.instance.order.tracksuit.group_sheet import (
	TeamInstanceTracksuitOrderGroupSheetSchemaCreate,
	TeamInstanceTracksuitOrderGroupSheetSchemaUpdate,
)




class CRUDTeamInstanceTracksuitOrderGroupSheet(
	CRUDBase[
		TeamInstanceTracksuitOrderGroupSheetModel,
		TeamInstanceTracksuitOrderGroupSheetSchemaCreate,
		TeamInstanceTracksuitOrderGroupSheetSchemaUpdate,
	]):
	
	pass



team_instance_tracksuit_order_group_sheet_crud = CRUDTeamInstanceTracksuitOrderGroupSheet(TeamInstanceTracksuitOrderGroupSheetModel)



