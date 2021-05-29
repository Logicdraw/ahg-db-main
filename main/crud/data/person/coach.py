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

from app.models.data.person.coach import CoachModel

from app.schemas.data.person.coach import (
	CoachSchemaCreate,
	CoachSchemaUpdate,
)




class CRUDCoach(
	CRUDBase[
		CoachModel,
		CoachSchemaCreate,
		CoachSchemaUpdate,
	]):
	
	pass



coach_crud = CRUDCoach(CoachModel)



