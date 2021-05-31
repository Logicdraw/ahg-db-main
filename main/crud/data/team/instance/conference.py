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

from main.models.data.team.instance.conference import ConferenceInstanceModel

from main.schemas.data.team.instance.conference import (
	ConferenceInstanceSchemaCreate,
	ConferenceInstanceSchemaUpdate,
)




class CRUDConferenceInstance(
	CRUDBase[
		ConferenceInstanceModel,
		ConferenceInstanceSchemaCreate,
		ConferenceInstanceSchemaUpdate,
	]):
	
	pass



conference_instance_crud = CRUDConferenceInstance(ConferenceInstanceModel)



