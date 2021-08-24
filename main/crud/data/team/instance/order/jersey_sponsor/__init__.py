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

from main.models.data.team.instance.order.tracksuit import TeamInstanceJerseySponsorOrderModel

from main.schemas.data.team.instance.order.tracksuit import (
	TeamInstanceJerseySponsorOrderSchemaCreate,
	TeamInstanceJerseySponsorOrderSchemaUpdate,
)




class CRUDTeamInstanceJerseySponsorOrder(
	CRUDBase[
		TeamInstanceJerseySponsorOrderModel,
		TeamInstanceJerseySponsorOrderSchemaCreate,
		TeamInstanceJerseySponsorOrderSchemaUpdate,
	]):
	
	pass



team_instance_tracksuit_order_crud = CRUDTeamInstanceJerseySponsorOrder(TeamInstanceJerseySponsorOrderModel)



