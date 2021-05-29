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

from app.models.data.team.instance.conference import ConferenceInstanceModel

from app.schemas.data.team.instance.conference import (
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



