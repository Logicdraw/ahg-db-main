from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GuardiansPlayersSchemaBase(BaseModel):
	pass



class GuardiansPlayersSchemaCreate(GuardiansPlayersSchemaBase):
	pass



class GuardiansPlayersSchemaUpdate(GuardiansPlayersSchemaBase):
	pass



class GuardiansPlayersSchemaInDBBase(GuardiansPlayersSchemaBase):
	id: int

	class Config:
		orm_mode = True



class GuardiansPlayersSchema(GuardiansPlayersSchemaInDBBase):
	pass



class GuardiansPlayersSchemaInDB(GuardiansPlayersSchemaInDBBase):
	pass


