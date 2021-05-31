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

from main.models.form.entry import FormEntryModel

from main.schemas.form.entry import (
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





