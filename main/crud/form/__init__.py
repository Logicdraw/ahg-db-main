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

from app.models.data.form import FormModel

from app.schemas.data.form import (
	FormSchemaCreate,
	FormSchemaUpdate,
)



class CRUDForm(
	CRUDBase[
		FormModel,
		FormSchemaCreate,
		FormSchemaUpdate,
	]):
	pass





form_crud = CRUDForm(FormModel)


