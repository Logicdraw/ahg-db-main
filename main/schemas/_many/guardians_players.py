from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GuardiansPlayersSchemaBase(BaseModel):
	guardian_id: Optional[int] = None
	player_id: Optional[int] = None
	role: Optional[str] = None
	is_emergency_contact: Optional[bool] = None



class GuardiansPlayersSchemaCreate(GuardiansPlayersSchemaBase):
	pass



class GuardiansPlayersSchemaUpdate(GuardiansPlayersSchemaBase):
	pass



class GuardiansPlayersSchemaInDBBase(GuardiansPlayersSchemaBase):

	class Config:
		orm_mode = True



class GuardiansPlayersSchema(GuardiansPlayersSchemaInDBBase):
	pass



class GuardiansPlayersSchemaInDB(GuardiansPlayersSchemaInDBBase):
	pass


