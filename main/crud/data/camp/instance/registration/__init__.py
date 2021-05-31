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

from main.models.data.camp.instance.registration import CampInstanceRegistrationModel

from main.schemas.data.camp.instance.registration import (
	CampInstanceRegistrationSchemaCreate,
	CampInstanceRegistrationSchemaUpdate,
)




class CRUDCampInstanceRegistration(
	CRUDBase[
		CampInstanceRegistrationModel,
		CampInstanceRegistrationSchemaCreate,
		CampInstanceRegistrationSchemaUpdate,
	]):
	
	pass



camp_instance_registration_crud = CRUDCampInstanceRegistration(CampInstanceRegistrationModel)



