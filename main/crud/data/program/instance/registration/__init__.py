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

from app.models.data.program.instance.registration import ProgramInstanceRegistrationModel

from app.schemas.data.program.instance.registration import (
	ProgramInstanceRegistrationSchemaCreate,
	ProgramInstanceRegistrationSchemaUpdate,
)




class CRUDProgramInstanceRegistration(
	CRUDBase[
		ProgramInstanceRegistrationModel,
		ProgramInstanceRegistrationSchemaCreate,
		ProgramInstanceRegistrationSchemaUpdate,
	]):
	
	pass



program_instance_registration_crud = CRUDProgramInstanceRegistration(ProgramInstanceRegistrationModel)



