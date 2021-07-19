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




class SpngSurveyCampInstanceSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	# default_camp_instance_id: Optional[int] = None
	pass



class SpngSurveyCampInstanceSchemaCreate(
	SpngSurveyCampInstanceSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	type: str = 'camp'



class SpngSurveyCampInstanceSchemaUpdate(
	SpngSurveyCampInstanceSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyCampInstanceSchemaInDBBase(
	SpngSurveyCampInstanceSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyCampInstanceSchema(
	SpngSurveyCampInstanceSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyCampInstanceSchemaInDB(
	SpngSurveyCampInstanceSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





