from typing import (
	Optional,
	Any,
	Dict,
	List,
)

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyQuestionSchemaBase(BaseModel):
	use_answer_text_mappings: Optional[bool] = None
	exclude_non_set_answer_text_mapping_keys: Optional[bool] = None
	shared_question_ids: Optional[List[int]] = None
	answer_text_mappings: Optional[Dict[Any, Any]] = None



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


