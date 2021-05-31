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

from main.models.form import FormModel

from main.schemas.form import (
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


