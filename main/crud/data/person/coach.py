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

from main.models.data.person.coach import CoachModel

from main.schemas.data.person.coach import (
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



