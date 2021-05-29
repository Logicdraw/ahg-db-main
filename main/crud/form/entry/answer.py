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

from app.models.data.form.entry.answer import (
	FormEntryAnswerModel,
	FormEntryAnswerInputModel,
	FormEntryAnswerTextareaModel,
	FormEntryAnswerSelectModel,
	FormEntryAnswerCheckboxModel,
	FormEntryAnswerRadioModel,
)

from app.schemas.data.form.entry.answer import (
	FormEntryAnswerSchemaCreate,
	FormEntryAnswerSchemaUpdate,
	FormEntryAnswerInputSchemaCreate,
	FormEntryAnswerInputSchemaUpdate,
	FormEntryAnswerTextareaSchemaCreate,
	FormEntryAnswerTextareaSchemaUpdate,
	FormEntryAnswerSelectSchemaCreate,
	FormEntryAnswerSelectSchemaUpdate,
	FormEntryAnswerCheckboxSchemaCreate,
	FormEntryAnswerCheckboxSchemaUpdate,
	FormEntryAnswerRadioSchemaCreate,
	FormEntryAnswerRadioSchemaUpdate,
)



class CRUDFormEntryAnswer(
	CRUDBase[
		FormEntryAnswerModel,
		FormEntryAnswerSchemaCreate,
		FormEntryAnswerSchemaUpdate,
	]):
	pass



class CRUDFormEntryAnswerInput(
	CRUDBase[
		FormEntryAnswerInputModel,
		FormEntryAnswerInputSchemaCreate,
		FormEntryAnswerInputSchemaUpdate,
	]):
	pass



class CRUDFormEntryAnswerTextarea(
	CRUDBase[
		FormEntryAnswerTextareaModel,
		FormEntryAnswerTextareaSchemaCreate,
		FormEntryAnswerTextareaSchemaUpdate,
	]):
	pass



class CRUDFormEntryAnswerSelect(
	CRUDBase[
		FormEntryAnswerSelectModel,
		FormEntryAnswerSelectSchemaCreate,
		FormEntryAnswerSelectSchemaUpdate,
	]):
	pass



class CRUDFormEntryAnswerCheckbox(
	CRUDBase[
		FormEntryAnswerCheckboxModel,
		FormEntryAnswerCheckboxSchemaCreate,
		FormEntryAnswerCheckboxSchemaUpdate,
	]):
	pass



class CRUDFormEntryAnswerRadio(
	CRUDBase[
		FormEntryAnswerRadioModel,
		FormEntryAnswerRadioSchemaCreate,
		FormEntryAnswerRadioSchemaUpdate,
	]):
	pass





form_entry_answer_crud = CRUDFormEntryAnswer(FormEntryAnswerModel)

form_entry_answer_input_crud = CRUDFormEntryAnswerInput(FormEntryAnswerInputModel)

form_entry_answer_textarea_crud = CRUDFormEntryAnswerTextarea(FormEntryAnswerTextareaModel)

form_entry_answer_select_crud = CRUDFormEntryAnswerSelect(FormEntryAnswerSelectModel)

form_entry_answer_checkbox_crud = CRUDFormEntryAnswerCheckbox(FormEntryAnswerCheckboxModel)

form_entry_answer_radio_crud = CRUDFormEntryAnswerRadio(FormEntryAnswerRadioModel)



# more...




