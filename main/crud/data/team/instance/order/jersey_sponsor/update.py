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

from main.models.data.team.instance.order.jersey_sponsor.update import TeamInstanceJerseySponsorOrderUpdateModel

from main.schemas.data.team.instance.order.jersey_sponsor.update import (
	TeamInstanceJerseySponsorOrderUpdateSchemaCreate,
	TeamInstanceJerseySponsorOrderUpdateSchemaUpdate,
)




class CRUDTeamInstanceJerseySponsorOrderUpdate(
	CRUDBase[
		TeamInstanceJerseySponsorOrderUpdateModel,
		TeamInstanceJerseySponsorOrderUpdateSchemaCreate,
		TeamInstanceJerseySponsorOrderUpdateSchemaUpdate,
	]):
	
	pass



team_instance_jersey_sponsor_order_update_crud = CRUDTeamInstanceJerseySponsorOrderUpdate(TeamInstanceJerseySponsorOrderUpdateModel)



