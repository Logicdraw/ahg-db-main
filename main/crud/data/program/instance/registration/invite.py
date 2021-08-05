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

from main.models.data.program.instance.registration.invite import ProgramInstanceRegistrationInviteModel

from main.schemas.data.program.instance.registration.invite import (
	ProgramInstanceRegistrationInviteSchemaCreate,
	ProgramInstanceRegistrationInviteSchemaUpdate,
)




class CRUDProgramInstanceRegistrationInvite(
	CRUDBase[
		ProgramInstanceRegistrationInviteModel,
		ProgramInstanceRegistrationInviteSchemaCreate,
		ProgramInstanceRegistrationInviteSchemaUpdate,
	]):
	
	pass



program_instance_registration_invite_crud = CRUDProgramInstanceRegistrationInvite(ProgramInstanceRegistrationInviteModel)



