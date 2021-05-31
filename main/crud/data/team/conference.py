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

from main.models.data.team.conference import ConferenceModel

from main.schemas.data.team.conference import (
	ConferenceSchemaCreate,
	ConferenceSchemaUpdate,
)




class CRUDConference(
	CRUDBase[
		ConferenceModel,
		ConferenceSchemaCreate,
		ConferenceSchemaUpdate,
	]):
	
	pass



conference_crud = CRUDConference(ConferenceModel)



