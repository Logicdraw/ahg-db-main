from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
	validator,
)


from main.config import settings



class UserSchemaBase(BaseModel):
	name: Optional[str] = None
	email: Optional[EmailStr] = None
	role: Optional[str] = None
	is_active: Optional[bool] = None



class UserSchemaCreate(UserSchemaBase):
	name: str
	email: EmailStr
	password: str
	confirm_password: str
	role: str = 'member'
	is_active: bool = True


	@validator('confirm_password')
	def password_matches(cls, v, values, **kwargs):
		if 'password' in values and v != values['password']:
			raise ValueError('Passwords do not match!')
		return v


	@validator('role')
	def role_in_list(cls, v):
		if v not in settings.USER_ROLES:
			raise ValueError('Not a valid role!')
		return v



class UserSchemaUpdate(UserSchemaBase):
	password: Optional[str] = None
	confirm_password: Optional[str] = None


	@validator('confirm_password')
	def password_matches(cls, v, values, **kwargs):
		if 'password' in values and v != values['password']:
			raise ValueError('Passwords do not match!')
		return v



class UserSchemaInDBBase(UserSchemaBase):
	id: int

	class Config:
		orm_mode = True



class UserSchema(UserSchemaInDBBase):
	pass



class UserSchemaInDB(UserSchemaInDBBase):
	password_hash: str


