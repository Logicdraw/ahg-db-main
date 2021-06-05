from typing import (
	Optional,
	Any,
	Dict,
)

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormQuestionSchemaBase(BaseModel):
	form_id: Optional[int] = None
	label: Optional[str] = None
	is_active: Optional[bool] = None



class FormQuestionSchemaCreate(FormQuestionSchemaBase):
	pass



class FormQuestionSchemaUpdate(FormQuestionSchemaBase):
	pass



class FormQuestionSchemaInDBBase(FormQuestionSchemaBase):
	id: int

	class Config:
		orm_mode = True



class FormQuestionSchema(FormQuestionSchemaInDBBase):
	pass



class FormQuestionSchemaInDB(FormQuestionSchemaInDBBase):
	pass





# Input --


class FormQuestionInputSchemaBase(
	FormQuestionSchemaBase,
):
	pass



class FormQuestionInputSchemaCreate(
	FormQuestionInputSchemaBase,
	FormQuestionSchemaCreate,
):
	pass



class FormQuestionInputSchemaUpdate(
	FormQuestionInputSchemaBase,
	FormQuestionSchemaUpdate,
):
	pass



class FormQuestionInputSchemaInDBBase(
	FormQuestionInputSchemaBase,
	FormQuestionSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormQuestionInputSchema(
	FormQuestionSchema,
	FormQuestionInputSchemaInDBBase,
):
	pass



class FormQuestionInputSchemaInDB(
	FormQuestionSchemaInDB,
	FormQuestionInputSchemaInDBBase,
):
	pass




# Textarea --


class FormQuestionTextareaSchemaBase(
	FormQuestionSchemaBase,
):
	pass



class FormQuestionTextareaSchemaCreate(
	FormQuestionTextareaSchemaBase,
	FormQuestionSchemaCreate,
):
	pass



class FormQuestionTextareaSchemaUpdate(
	FormQuestionTextareaSchemaBase,
	FormQuestionSchemaUpdate,
):
	pass



class FormQuestionTextareaSchemaInDBBase(
	FormQuestionTextareaSchemaBase,
	FormQuestionSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormQuestionTextareaSchema(
	FormQuestionSchema,
	FormQuestionTextareaSchemaInDBBase,
):
	pass



class FormQuestionTextareaSchemaInDB(
	FormQuestionSchemaInDB,
	FormQuestionTextareaSchemaInDBBase,
):
	pass




# Select --


class FormQuestionSelectSchemaBase(
	FormQuestionSchemaBase,
):
	select_is_multiple: Optional[bool] = None
	select_answers: Optional[Dict[Any, Any]] = None



class FormQuestionSelectSchemaCreate(
	FormQuestionSelectSchemaBase,
	FormQuestionSchemaCreate,
):
	pass



class FormQuestionSelectSchemaUpdate(
	FormQuestionSelectSchemaBase,
	FormQuestionSchemaUpdate,
):
	pass



class FormQuestionSelectSchemaInDBBase(
	FormQuestionSelectSchemaBase,
	FormQuestionSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormQuestionSelectSchema(
	FormQuestionSchema,
	FormQuestionSelectSchemaInDBBase,
):
	pass



class FormQuestionSelectSchemaInDB(
	FormQuestionSchemaInDB,
	FormQuestionSelectSchemaInDBBase,
):
	pass





# Checkbox --


class FormQuestionCheckboxSchemaBase(
	FormQuestionSchemaBase,
):
	pass



class FormQuestionCheckboxSchemaCreate(
	FormQuestionCheckboxSchemaBase,
	FormQuestionSchemaCreate,
):
	pass



class FormQuestionCheckboxSchemaUpdate(
	FormQuestionCheckboxSchemaBase,
	FormQuestionSchemaUpdate,
):
	pass



class FormQuestionCheckboxSchemaInDBBase(
	FormQuestionCheckboxSchemaBase,
	FormQuestionSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormQuestionCheckboxSchema(
	FormQuestionSchema,
	FormQuestionCheckboxSchemaInDBBase,
):
	pass



class FormQuestionCheckboxSchemaInDB(
	FormQuestionSchemaInDB,
	FormQuestionCheckboxSchemaInDBBase,
):
	pass




# Radio --


class FormQuestionRadioSchemaBase(
	FormQuestionSchemaBase,
):
	radio_answers: Optional[Any] = None



class FormQuestionRadioSchemaCreate(
	FormQuestionRadioSchemaBase,
	FormQuestionSchemaCreate,
):
	pass



class FormQuestionRadioSchemaUpdate(
	FormQuestionRadioSchemaBase,
	FormQuestionSchemaUpdate,
):
	pass



class FormQuestionRadioSchemaInDBBase(
	FormQuestionRadioSchemaBase,
	FormQuestionSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class FormQuestionRadioSchema(
	FormQuestionSchema,
	FormQuestionRadioSchemaInDBBase,
):
	pass



class FormQuestionRadioSchemaInDB(
	FormQuestionSchemaInDB,
	FormQuestionRadioSchemaInDBBase,
):
	pass






