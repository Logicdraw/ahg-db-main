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

from main.models.meta.spng import SpngMetaModel

from main.schemas.meta.spng import (
	SpngMetaSchemaCreate,
	SpngMetaSchemaUpdate,
)




class CRUDSpngMeta(
	CRUDBase[
		SpngMetaModel,
		SpngMetaSchemaCreate,
		SpngMetaSchemaUpdate,
	]):
	
	pass



spng_meta_crud = CRUDSpngMeta(SpngMetaModel)



