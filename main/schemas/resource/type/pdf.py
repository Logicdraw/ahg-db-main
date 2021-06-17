from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.resource import (
	ResourceBaseSchemaBase,
	ResourceBaseSchemaCreate,
	ResourceBaseSchemaUpdate,
	ResourceBaseSchemaInDBBase,
	ResourceBaseSchema,
	ResourceBaseSchemaInDB,
)




class ResourcePDFSchemaBase(
	ResourceBaseSchemaBase,
):
	pdf_url: Optional[str] = None



class ResourcePDFSchemaCreate(
	ResourcePDFSchemaBase,
	ResourceBaseSchemaCreate,
):
	pass



class ResourcePDFSchemaUpdate(
	ResourcePDFSchemaBase,
	ResourceBaseSchemaUpdate,
):
	pass



class ResourcePDFSchemaInDBBase(
	ResourcePDFSchemaBase,
	ResourceBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class ResourcePDFSchema(
	ResourcePDFSchemaInDBBase,
	ResourceBaseSchema,
):
	pass



class ResourcePDFSchemaInDB(
	ResourcePDFSchemaInDBBase,
	ResourceBaseSchemaInDB,
):
	pass





