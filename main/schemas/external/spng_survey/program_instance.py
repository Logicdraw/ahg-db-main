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




class SpngSurveyProgramInstanceSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	# default_program_instance_id: Optional[int] = None
	pass



class SpngSurveyProgramInstanceSchemaCreate(
	SpngSurveyProgramInstanceSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	type: str = 'program_instance'



class SpngSurveyProgramInstanceSchemaUpdate(
	SpngSurveyProgramInstanceSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyProgramInstanceSchemaInDBBase(
	SpngSurveyProgramInstanceSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyProgramInstanceSchema(
	SpngSurveyProgramInstanceSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyProgramInstanceSchemaInDB(
	SpngSurveyProgramInstanceSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





