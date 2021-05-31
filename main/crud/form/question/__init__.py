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


from main.models.form.question import (
	FormQuestionModel,
	FormQuestionInputModel,
	FormQuestionTextareaModel,
	FormQuestionSelectModel,
	FormQuestionCheckboxModel,
	FormQuestionRadioModel,
)

from main.schemas.form.question import (
	FormQuestionSchemaCreate,
	FormQuestionSchemaUpdate,
	FormQuestionInputSchemaCreate,
	FormQuestionInputSchemaUpdate,
	FormQuestionTextareaSchemaCreate,
	FormQuestionTextareaSchemaUpdate,
	FormQuestionSelectSchemaCreate,
	FormQuestionSelectSchemaUpdate,
	FormQuestionCheckboxSchemaCreate,
	FormQuestionCheckboxSchemaUpdate,
	FormQuestionRadioSchemaCreate,
	FormQuestionRadioSchemaUpdate,
)




class CRUDFormQuestion(
	CRUDBase[
		FormQuestionModel,
		FormQuestionSchemaCreate,
		FormQuestionSchemaUpdate,
	]):
	pass




class CRUDFormQuestionInput(
	CRUDBase[
		FormQuestionInputModel,
		FormQuestionInputSchemaCreate,
		FormQuestionInputSchemaUpdate,
	]):
	pass




class CRUDFormQuestionTextarea(
	CRUDBase[
		FormQuestionTextareaModel,
		FormQuestionTextareaSchemaCreate,
		FormQuestionTextareaSchemaUpdate,
	]):
	pass



class CRUDFormQuestionSelect(
	CRUDBase[
		FormQuestionSelectModel,
		FormQuestionSelectSchemaCreate,
		FormQuestionSelectSchemaUpdate,
	]):
	pass



class CRUDFormQuestionCheckbox(
	CRUDBase[
		FormQuestionCheckboxModel,
		FormQuestionCheckboxSchemaCreate,
		FormQuestionCheckboxSchemaUpdate,
	]):
	pass



class CRUDFormQuestionRadio(
	CRUDBase[
		FormQuestionRadioModel,
		FormQuestionRadioSchemaCreate,
		FormQuestionRadioSchemaUpdate,
	]):
	pass






form_question_crud = CRUDFormQuestion(FormQuestionModel)

form_question_input_crud = CRUDFormQuestionInput(FormQuestionInputModel)

form_question_textarea_crud = CRUDFormQuestionTextarea(FormQuestionInputModel)

form_question_select_crud = CRUDFormQuestionSelect(FormQuestionSelectModel)

form_question_radio_crud = CRUDFormQuestionRadio(FormQuestionRadioModel)



