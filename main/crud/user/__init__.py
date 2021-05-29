from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy import (
	func,
	or_,
)


from app.security import (
	get_password_hash,
	verify_password,
)


from app.crud.base import CRUDBase

from app.models.user import UserModel

from app.schemas.user import (
	UserSchemaCreate,
	UserSchemaUpdate,
)





class CRUDUser(
	CRUDBase[
		UserModel,
		UserSchemaCreate,
		UserSchemaUpdate,
	]):

	
	async def create(
		self,
		db: AsyncSession,
		*,
		obj_in: UserSchemaCreate,
	) -> UserModel:
		# Create --

		db_obj = UserModel(
			email=obj_in.email,
			password_hash=get_password_hash(obj_in.password),
			name=obj_in.name,
			role=obj_in.role,
		)

		db.add(db_obj)

		await db.commit()

		return db_obj



	async def update(
		self,
		db: AsyncSession,
		*,
		db_obj: UserModel,
		obj_in: Union[UserSchemaUpdate, Dict[str, Any]],
	) -> UserModel:
		# Update --

		if isinstance(obj_in, dict):
			update_data = obj_in
		else:
			update_data = obj_in.dict(exclude_unset=True)

		try:
			if update_data['password']:
				password_hash = get_password_hash(update_data['password'])
				del update_data['password']
				update_data['password_hash'] = password_hash
		except KeyError:
			pass


		result = super().\
					update(
						db=db,
						db_obj=db_obj,
						obj_in=update_data,
					)

		return result



	async def get_by_email(
		self,
		db: AsyncSession,
		*,
		email: str,
	) -> Optional[UserModel]:
		# Get by email --

		result = await db.execute(
			select(UserModel).\
			filter(
				func.lower(UserModel.email) == func.lower(email),
			)
		)

		return result.scalars().first()



	async def authenticate(
		self,
		db: AsyncSession,
		*,
		email: str,
		password: str,
	) -> Optional[UserModel]:
		# Authenticate --

		user = self.get_by_email(db=db, email=email)

		if not user:
			return None

		if not verify_password(password, user.password_hash):
			return None


		return user



	def is_active(
		self,
		user: UserModel,
	) -> bool:
		# Is active --

		return user.is_active



	def is_role(
		self,
		user: UserModel,
		role: str,
	) -> bool:
		# Is role --

		return user.role == role



	
user_crud = CRUDUser(UserModel)



