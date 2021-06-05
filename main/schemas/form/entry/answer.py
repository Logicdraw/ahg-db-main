from typing import (
	Optional,
	Any,
)

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormEntryAnswerSchemaBase(BaseModel):
	entry_id: Optional[int] = None
	question_id: Optional[int] = None



class FormEntryAnswerSchemaCreate(FormEntryAnswerSchemaBase):
	pass



class FormEntryAnswerSchemaUpdate(FormEntryAnswerSchemaBase):
	pass



class FormEntryAnswerSchemaInDBBase(FormEntryAnswerSchemaBase):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerSchema(FormEntryAnswerSchemaInDBBase):
	pass



class FormEntryAnswerSchemaInDB(FormEntryAnswerSchemaInDBBase):
	pass





# Other (Inheritance --)


# Input --

class FormEntryAnswerInputSchemaBase(
	FormEntryAnswerSchemaBase,
):
	input_answer: Optional[str] = None



class FormEntryAnswerInputSchemaCreate(
	FormEntryAnswerInputSchemaBase,
	FormEntryAnswerSchemaCreate,
):
	pass



class FormEntryAnswerInputSchemaUpdate(
	FormEntryAnswerInputSchemaBase,
	FormEntryAnswerSchemaUpdate,
):
	pass



class FormEntryAnswerInputSchemaInDBBase(
	FormEntryAnswerInputSchemaBase,
	FormEntryAnswerSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerInputSchema(
	FormEntryAnswerSchema,
	FormEntryAnswerInputSchemaInDBBase,
):
	pass



class FormEntryAnswerInputSchemaInDB(
	FormEntryAnswerSchemaInDB,
	FormEntryAnswerInputSchemaInDBBase,
):
	pass




# Textarea --


class FormEntryAnswerTextareaSchemaBase(
	FormEntryAnswerSchemaBase,
):
	textarea_answer: Optional[str] = None



class FormEntryAnswerTextareaSchemaCreate(
	FormEntryAnswerTextareaSchemaBase,
	FormEntryAnswerSchemaCreate,
):
	pass



class FormEntryAnswerTextareaSchemaUpdate(
	FormEntryAnswerTextareaSchemaBase,
	FormEntryAnswerSchemaUpdate,
):
	pass



class FormEntryAnswerTextareaSchemaInDBBase(
	FormEntryAnswerTextareaSchemaBase,
	FormEntryAnswerSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerTextareaSchema(
	FormEntryAnswerSchema,
	FormEntryAnswerTextareaSchemaInDBBase,
):
	pass



class FormEntryAnswerTextareaSchemaInDB(
	FormEntryAnswerSchemaInDB,
	FormEntryAnswerTextareaSchemaInDBBase,
):
	pass




# Select --


class FormEntryAnswerSelectSchemaBase(
	FormEntryAnswerSchemaBase,
):
	select_selected: Optional[Any] = None



class FormEntryAnswerSelectSchemaCreate(
	FormEntryAnswerSelectSchemaBase,
	FormEntryAnswerSchemaCreate,
):
	pass



class FormEntryAnswerSelectSchemaUpdate(
	FormEntryAnswerSelectSchemaBase,
	FormEntryAnswerSchemaUpdate,
):
	pass



class FormEntryAnswerSelectSchemaInDBBase(
	FormEntryAnswerSelectSchemaBase,
	FormEntryAnswerSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerSelectSchema(
	FormEntryAnswerSchema,
	FormEntryAnswerSelectSchemaInDBBase,
):
	pass



class FormEntryAnswerSelectSchemaInDB(
	FormEntryAnswerSchemaInDB,
	FormEntryAnswerSelectSchemaInDBBase,
):
	pass





# Checkbox --


class FormEntryAnswerCheckboxSchemaBase(
	FormEntryAnswerSchemaBase,
):
	checkbox_checked: Optional[str] = None



class FormEntryAnswerCheckboxSchemaCreate(
	FormEntryAnswerCheckboxSchemaBase,
	FormEntryAnswerSchemaCreate,
):
	pass



class FormEntryAnswerCheckboxSchemaUpdate(
	FormEntryAnswerCheckboxSchemaBase,
	FormEntryAnswerSchemaUpdate,
):
	pass



class FormEntryAnswerCheckboxSchemaInDBBase(
	FormEntryAnswerCheckboxSchemaBase,
	FormEntryAnswerSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerCheckboxSchema(
	FormEntryAnswerSchema,
	FormEntryAnswerCheckboxSchemaInDBBase,
):
	pass



class FormEntryAnswerCheckboxSchemaInDB(
	FormEntryAnswerSchemaInDB,
	FormEntryAnswerCheckboxSchemaInDBBase,
):
	pass




# Radio --


class FormEntryAnswerRadioSchemaBase(
	FormEntryAnswerSchemaBase,
):
	radio_selected: Optional[Any] = None



class FormEntryAnswerRadioSchemaCreate(
	FormEntryAnswerRadioSchemaBase,
	FormEntryAnswerSchemaCreate,
):
	pass



class FormEntryAnswerRadioSchemaUpdate(
	FormEntryAnswerRadioSchemaBase,
	FormEntryAnswerSchemaUpdate,
):
	pass



class FormEntryAnswerRadioSchemaInDBBase(
	FormEntryAnswerRadioSchemaBase,
	FormEntryAnswerSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormEntryAnswerRadioSchema(
	FormEntryAnswerSchema,
	FormEntryAnswerRadioSchemaInDBBase,
):
	pass



class FormEntryAnswerRadioSchemaInDB(
	FormEntryAnswerSchemaInDB,
	FormEntryAnswerRadioSchemaInDBBase,
):
	pass




