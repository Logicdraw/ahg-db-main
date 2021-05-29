from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaBase,
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
	SpngSurveyBaseSchemaInDBBase,
	SpngSurveyBaseSchema,
	SpngSurveyBaseSchemaInDB,
)




class SpngSurveyProgramSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	pass



class SpngSurveyProgramSchemaCreate(
	SpngSurveyProgramSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	pass



class SpngSurveyProgramSchemaUpdate(
	SpngSurveyProgramSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyProgramSchemaInDBBase(
	SpngSurveyProgramSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyProgramSchema(
	SpngSurveyProgramSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyProgramSchemaInDB(
	SpngSurveyProgramSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





