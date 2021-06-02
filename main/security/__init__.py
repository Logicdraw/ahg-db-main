# For testing purposes ONLY --- !

from datetime import (
	datetime,
	timedelta,
)

from typing import (
	Any,
	Union,
)


from jose import jwt

from passlib.context import CryptContext

from main.config import settings



pwd_context = CryptContext(
	schemes=['bcrypt'],
	deprecated='auto',
)



def verify_password(
	plain_password: str,
	hashed_password: str,
) -> bool:
	"""
	Verify password
	"""

	return pwd_context.verify(plain_password, hashed_password)



def get_password_hash(password: str) -> str:
	"""
	Get password hash
	"""

	return pwd_context.hash(password)



