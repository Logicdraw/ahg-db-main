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

from app.models.data.program.group.instance import ProgramGroupInstanceModel

from app.schemas.data.program.group.instance import (
	ProgramGroupInstanceSchemaCreate,
	ProgramGroupInstanceSchemaUpdate,
)




class CRUDProgramGroupInstance(
	CRUDBase[
		ProgramGroupInstanceModel,
		ProgramGroupInstanceSchemaCreate,
		ProgramGroupInstanceSchemaUpdate,
	]):
	
	pass



program_group_instance_crud = CRUDProgramGroupInstance(ProgramGroupInstanceModel)



