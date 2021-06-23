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
	# default_program_instance_id: Optional[int] = None
	pass



class SpngSurveyProgramSchemaCreate(
	SpngSurveyProgramSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	type: str = 'program'



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





