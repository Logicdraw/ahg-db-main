from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyQuestionTableMapSchemaBase(BaseModel):
	db_table_name: Optional[str] = None
	db_table_column_name: Optional[str] = None
	spng_survey_question_id: Optional[int] = None



class SpngSurveyQuestionTableMapSchemaCreate(SpngSurveyQuestionTableMapSchemaBase):
	pass



class SpngSurveyQuestionTableMapSchemaUpdate(SpngSurveyQuestionTableMapSchemaBase):
	pass



class SpngSurveyQuestionTableMapSchemaInDBBase(SpngSurveyQuestionTableMapSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyQuestionTableMapSchema(SpngSurveyQuestionTableMapSchemaInDBBase):
	pass



class SpngSurveyQuestionTableMapSchemaInDB(SpngSurveyQuestionTableMapSchemaInDBBase):
	pass


