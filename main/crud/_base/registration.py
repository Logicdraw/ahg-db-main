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

from app.models._base.registration import RegistrationBaseModel

from app.schemas._base.registration import (
	RegistrationBaseSchemaCreate,
	RegistrationBaseSchemaUpdate,
)




class CRUDRegistrationBase(
	CRUDBase[
		RegistrationBaseModel,
		RegistrationBaseSchemaCreate,
		RegistrationBaseSchemaUpdate,
	]):
	
	pass



registration_base_crud = CRUDRegistrationBase(RegistrationBaseModel)



