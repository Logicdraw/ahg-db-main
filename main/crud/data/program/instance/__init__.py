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

from app.models.data.program.instance import ProgramInstanceModel

from app.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
)




class CRUDProgramInstance(
	CRUDBase[
		ProgramInstanceModel,
		ProgramInstanceSchemaCreate,
		ProgramInstanceSchemaUpdate,
	]):
	
	pass



program_instance_crud = CRUDProgramInstance(ProgramInstanceModel)



