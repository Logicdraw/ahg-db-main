from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormEntryAnswerSchemaBase(BaseModel):
	pass



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
	pass



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
	pass



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
	pass



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
	pass



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
	pass



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




