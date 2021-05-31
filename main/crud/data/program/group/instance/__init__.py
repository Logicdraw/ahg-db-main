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

from main.models.data.program.group.instance import ProgramGroupInstanceModel

from main.schemas.data.program.group.instance import (
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



