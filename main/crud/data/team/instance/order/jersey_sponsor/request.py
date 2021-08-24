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

from main.models.data.team.instance.order.jersey_sponsor.request import TeamInstanceJerseySponsorOrderRequestModel

from main.schemas.data.team.instance.order.jersey_sponsor.request import (
	TeamInstanceJerseySponsorOrderRequestSchemaCreate,
	TeamInstanceJerseySponsorOrderRequestSchemaUpdate,
)




class CRUDTeamInstanceJerseySponsorOrderRequest(
	CRUDBase[
		TeamInstanceJerseySponsorOrderRequestModel,
		TeamInstanceJerseySponsorOrderRequestSchemaCreate,
		TeamInstanceJerseySponsorOrderRequestSchemaUpdate,
	]):
	
	pass



team_instance_jersey_sponsor_order_request_crud = CRUDTeamInstanceJerseySponsorOrderRequest(TeamInstanceJerseySponsorOrderRequestModel)



