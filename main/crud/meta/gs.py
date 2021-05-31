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

from main.models.meta.gs import GSMetaModel

from main.schemas.meta.gs import (
	GSMetaSchemaCreate,
	GSMetaSchemaUpdate,
)




class CRUDGSMeta(
	CRUDBase[
		GSMetaModel,
		GSMetaSchemaCreate,
		GSMetaSchemaUpdate,
	]):
	
	pass



gs_meta_crud = CRUDGSMeta(GSMetaModel)



