from typing import (
	Optional,
	Any,
)

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyQuestionSchemaBase(BaseModel):
	use_answer_text_mappings: Optional[str] = None
	shared_question_ids: Optional[Any] = None
	answer_text_mappings: Optional[str] = None



class SpngSurveyQuestionSchemaCreate(SpngSurveyQuestionSchemaBase):
	pass



class SpngSurveyQuestionSchemaUpdate(SpngSurveyQuestionSchemaBase):
	pass



class SpngSurveyQuestionSchemaInDBBase(SpngSurveyQuestionSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyQuestionSchema(SpngSurveyQuestionSchemaInDBBase):
	pass



class SpngSurveyQuestionSchemaInDB(SpngSurveyQuestionSchemaInDBBase):
	pass


