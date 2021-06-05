from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession



from main.crud.base import CRUDBase

from main.models._many.program_instances_coaches import ProgramInstancesCoachesModel

from main.schemas._many.program_instances_coaches import (
	ProgramInstancesCoachesSchemaCreate,
	ProgramInstancesCoachesSchemaUpdate,
)



class CRUDProgramInstancesCoaches(
	CRUDBase[
		ProgramInstancesCoachesModel,
		ProgramInstancesCoachesSchemaCreate,
		ProgramInstancesCoachesSchemaUpdate,
	]):




program_instances_coaches_crud = CRUDProgramInstancesCoaches(ProgramInstancesCoachesModel)



