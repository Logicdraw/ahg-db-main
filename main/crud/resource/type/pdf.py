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

from main.models.resource.type.pdf import ResourcePDFModel

from main.schemas.resource.type.pdf import (
	ResourcePDFSchemaCreate,
	ResourcePDFSchemaUpdate,
)




class CRUDResourcePDF(
	CRUDBase[
		ResourcePDFModel,
		ResourcePDFSchemaCreate,
		ResourcePDFSchemaUpdate,
	]):
	
	pass



resource_pdf_crud = CRUDResourcePDF(ResourcePDFModel)



