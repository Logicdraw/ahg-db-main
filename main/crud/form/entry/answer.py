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

from main.models.form.entry.answer import (
	FormEntryAnswerInputModel,
	FormEntryAnswerTextareaModel,
	FormEntryAnswerSelectModel,
	FormEntryAnswerCheckboxModel,
	FormEntryAnswerRadioModel,
)

from main.schemas.form.entry.answer import (
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




form_entry_answer_input_crud = CRUDFormEntryAnswerInput(FormEntryAnswerInputModel)

form_entry_answer_textarea_crud = CRUDFormEntryAnswerTextarea(FormEntryAnswerTextareaModel)

form_entry_answer_select_crud = CRUDFormEntryAnswerSelect(FormEntryAnswerSelectModel)

form_entry_answer_checkbox_crud = CRUDFormEntryAnswerCheckbox(FormEntryAnswerCheckboxModel)

form_entry_answer_radio_crud = CRUDFormEntryAnswerRadio(FormEntryAnswerRadioModel)



# more...




