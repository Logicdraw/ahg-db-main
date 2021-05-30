from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceSchemaBase(BaseModel):
	team_id: Optional[int] = None
	division_id: Optional[int] = None
	conference_id: Optional[int] = None
	league_id: Optional[int] = None
	season_id: Optional[int] = None
	year_start: Optional[str] = None
	year_end: Optional[str] = None
	birth_year: Optional[int] = None
	se_name_snake: Optional[str] = None
	se_shared_question_id: Optional[int] = None
	gs_team_id: Optional[int]
	number_of_tracksuits_available: Optional[int] = None
	jersey_numbers_options: Optional[str] = None
	has_jersey_size_option: Optional[bool] = None
	jersey_sizes_options: Optional[str] = None
	registrations_needs_jersey_default_value: Optional[bool] = None
	has_socks_size_option: Optional[bool] = None
	socks_sizes_options: Optional[str] = None
	registrations_needs_socks_default_value: Optional[bool] = None



class TeamInstanceSchemaCreate(TeamInstanceSchemaBase):
	pass



class TeamInstanceSchemaUpdate(TeamInstanceSchemaBase):
	pass



class TeamInstanceSchemaInDBBase(TeamInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceSchema(TeamInstanceSchemaInDBBase):
	pass



class TeamInstanceSchemaInDB(TeamInstanceSchemaInDBBase):
	pass


