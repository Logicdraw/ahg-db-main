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

from main.models._base.registration import RegistrationBaseModel

from main.schemas._base.registration import (
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



