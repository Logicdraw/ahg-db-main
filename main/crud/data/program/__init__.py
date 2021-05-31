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

from main.models.data.program import ProgramModel

from main.schemas.data.program import (
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



