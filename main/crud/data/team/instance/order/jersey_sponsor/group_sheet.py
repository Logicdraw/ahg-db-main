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

from main.models.data.team.instance.order.jersey_sponsor.group_sheet import TeamInstanceJerseySponsorOrderGroupSheetModel

from main.schemas.data.team.instance.order.jersey_sponsor.group_sheet import (
	TeamInstanceJerseySponsorOrderGroupSheetSchemaCreate,
	TeamInstanceJerseySponsorOrderGroupSheetSchemaUpdate,
)




class CRUDTeamInstanceJerseySponsorOrderGroupSheet(
	CRUDBase[
		TeamInstanceJerseySponsorOrderGroupSheetModel,
		TeamInstanceJerseySponsorOrderGroupSheetSchemaCreate,
		TeamInstanceJerseySponsorOrderGroupSheetSchemaUpdate,
	]):
	
	pass



team_instance_jersey_sponsor_order_group_sheet_crud = CRUDTeamInstanceJerseySponsorOrderGroupSheet(TeamInstanceJerseySponsorOrderGroupSheetModel)



