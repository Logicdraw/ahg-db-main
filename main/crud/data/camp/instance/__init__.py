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

from app.models.data.camp.instance import CampInstanceModel

from app.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
)




class CRUDCampInstance(
	CRUDBase[
		CampInstanceModel,
		CampInstanceSchemaCreate,
		CampInstanceSchemaUpdate,
	]):
	
	pass



camp_instance_crud = CRUDCampInstance(CampInstanceModel)



