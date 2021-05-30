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




class SpngSurveyCampSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	default_camp_instance_id: Optional[int] = None



class SpngSurveyCampSchemaCreate(
	SpngSurveyCampSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	pass



class SpngSurveyCampSchemaUpdate(
	SpngSurveyCampSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyCampSchemaInDBBase(
	SpngSurveyCampSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyCampSchema(
	SpngSurveyCampSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyCampSchemaInDB(
	SpngSurveyCampSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





