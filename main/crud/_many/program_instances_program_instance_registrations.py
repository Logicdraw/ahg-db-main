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

from main.models._many.program_instances_program_instance_registrations import ProgramInstancesProgramInstanceRegistrationsModel

from main.schemas._many.program_instances_program_instance_registrations import (
	ProgramInstancesProgramInstanceRegistrationsSchemaCreate,
	ProgramInstancesProgramInstanceRegistrationsSchemaUpdate,
)



class CRUDProgramInstancesProgramInstanceRegistrations(
	CRUDBase[
		ProgramInstancesProgramInstanceRegistrationsModel,
		ProgramInstancesProgramInstanceRegistrationsSchemaCreate,
		ProgramInstancesProgramInstanceRegistrationsSchemaUpdate,
	]):
	
	pass



program_instances_program_instance_registrations_crud = CRUDProgramInstancesProgramInstanceRegistrations(ProgramInstancesProgramInstanceRegistrationsModel)



