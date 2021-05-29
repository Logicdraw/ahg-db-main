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

from app.models.data.program import ProgramModel

from app.schemas.data.program import (
	ProgramSchemaCreate,
	ProgramSchemaUpdate,
)




class CRUDProgram(
	CRUDBase[
		ProgramModel,
		ProgramSchemaCreate,
		ProgramSchemaUpdate,
	]):
	
	pass



program_crud = CRUDProgram(ProgramModel)



