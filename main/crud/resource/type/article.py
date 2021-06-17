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

from main.models.resource.type.article import ResourceArticleModel

from main.schemas.resource.type.article import (
	ResourceArticleSchemaCreate,
	ResourceArticleSchemaUpdate,
)




class CRUDResourceArticle(
	CRUDBase[
		ResourceArticleModel,
		ResourceArticleSchemaCreate,
		ResourceArticleSchemaUpdate,
	]):
	
	pass



resource_article_crud = CRUDResourceArticle(ResourceArticleModel)



