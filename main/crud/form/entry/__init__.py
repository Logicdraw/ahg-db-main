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

from app.models.data.form.entry import FormEntryModel

from app.schemas.data.form.entry import (
	FormEntrySchemaCreate,
	FormEntrySchemaUpdate,
)



class CRUDFormEntry(
	CRUDBase[
		FormEntryModel,
		FormEntrySchemaCreate,
		FormEntrySchemaUpdate,
	]):
	pass





form_entry_crud = CRUDFormEntry(FormEntryModel)





