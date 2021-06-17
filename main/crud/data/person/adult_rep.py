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

from main.models.data.person.adult_rep import AdultRepModel

from main.schemas.data.person.adult_rep import (
	AdultRepSchemaCreate,
	AdultRepSchemaUpdate,
)




class CRUDAdultRep(
	CRUDBase[
		AdultRepModel,
		AdultRepSchemaCreate,
		AdultRepSchemaUpdate,
	]):
	
	pass



adult_rep_crud = CRUDAdultRep(AdultRepModel)



