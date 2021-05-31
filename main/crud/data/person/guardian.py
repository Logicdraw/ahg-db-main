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

from main.models.data.person.guardian import GuardianModel

from main.schemas.data.person.guardian import (
	GuardianSchemaCreate,
	GuardianSchemaUpdate,
)




class CRUDGuardian(
	CRUDBase[
		GuardianModel,
		GuardianSchemaCreate,
		GuardianSchemaUpdate,
	]):
	
	pass



guardian_crud = CRUDGuardian(GuardianModel)



