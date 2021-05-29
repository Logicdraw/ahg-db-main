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

from app.models.data.program.group import ProgramGroupModel

from app.schemas.data.program.group import (
	ProgramGroupSchemaCreate,
	ProgramGroupSchemaUpdate,
)




class CRUDProgramGroup(
	CRUDBase[
		ProgramGroupModel,
		ProgramGroupSchemaCreate,
		ProgramGroupSchemaUpdate,
	]):
	
	pass



program_group_crud = CRUDProgramGroup(ProgramGroupModel)



