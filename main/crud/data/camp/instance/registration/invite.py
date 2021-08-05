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

from main.models.data.camp.instance.registration.invite import CampInstanceRegistrationInviteModel

from main.schemas.data.camp.instance.registration.invite import (
	CampInstanceRegistrationInviteSchemaCreate,
	CampInstanceRegistrationInviteSchemaUpdate,
)




class CRUDCampInstanceRegistrationInvite(
	CRUDBase[
		CampInstanceRegistrationInviteModel,
		CampInstanceRegistrationInviteSchemaCreate,
		CampInstanceRegistrationInviteSchemaUpdate,
	]):
	
	pass



camp_instance_registration_invite_crud = CRUDCampInstanceRegistrationInvite(CampInstanceRegistrationInviteModel)



