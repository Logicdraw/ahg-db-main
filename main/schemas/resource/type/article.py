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




class ResourceArticleSchemaBase(
	ResourceBaseSchemaBase,
):
	article_body: Optional[str] = None



class ResourceArticleSchemaCreate(
	ResourceArticleSchemaBase,
	ResourceBaseSchemaCreate,
):
	pass



class ResourceArticleSchemaUpdate(
	ResourceArticleSchemaBase,
	ResourceBaseSchemaUpdate,
):
	pass



class ResourceArticleSchemaInDBBase(
	ResourceArticleSchemaBase,
	ResourceBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class ResourceArticleSchema(
	ResourceArticleSchemaInDBBase,
	ResourceBaseSchema,
):
	pass



class ResourceArticleSchemaInDB(
	ResourceArticleSchemaInDBBase,
	ResourceBaseSchemaInDB,
):
	pass





