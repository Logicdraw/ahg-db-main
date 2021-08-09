# !!! -- For TESTING purposes ONLY -- !!!
# !!! -- All real AUTH will be done through AUTH Microservice -- !!!


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



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
	schemes=["bcrypt"],
	deprecated="auto",
)


ALGORITHM = 'HS256'





def encode_token(
	token: str,
) -> str:
	# Encode access token --

	encoded_jwt = jwt.encode(
		{
			'sub': token,
		},
		settings.SECRET_KEY.get_secret_value(),
		algorithm='HS256',
	)
	return encoded_jwt



def token_decoded(
	token_encoded: str,
) -> str:
	# Decoded access token --

	try:
		token_decoded = jwt.decode(
			token_encoded,
			settings.SECRET_KEY.get_secret_value(),
			algorithms=["HS256"],
		)
		return token_decoded['sub']
	except jwt.JWTError:
		return None






def create_access_token(
	subject: Union[str, Any],
	expires_delta: timedelta = None,
) -> str:
	"""
	Create access token.

	:return: str
	"""

	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(
			minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
		)

	to_encode = {"exp": expire, "sub": str(subject)}
	
	encoded_jwt = jwt.encode(
		to_encode,
		settings.SECRET_KEY.get_secret_value(),
		algorithm=ALGORITHM,
	)

	return encoded_jwt




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



