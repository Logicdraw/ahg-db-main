from typing import (
	Any,
	Dict,
	Generic,
	List,
	Optional,
	Type,
	TypeVar,
	Union,
)

from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


from main.database.base import Base




ModelType = TypeVar('ModelType', bound=Base)

CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)




class CRUDBase(
	Generic[
		ModelType,
		CreateSchemaType,
		UpdateSchemaType,
	]):
	

	def __init__(
		self,
		model: Type[ModelType],
	) -> None:
		self.model = model



	async def get(
		self,
		db: AsyncSession,
		*args,
		**kwargs,
	) -> Optional[ModelType]:
		# Get --

		result = await db.execute(
			select(self.model).\
			filter(*args).\
			filter_by(**kwargs)
		)

		return result.scalars().first()


	def get_sync(
		self,
		db: AsyncSession,
		*args,
		**kwargs,
	) -> Optional[ModelType]:
		# Get Sync --

		result = db.execute(
			select(self.model).\
			filter(*args).\
			filter_by(**kwargs)
		)

		return result.scalars().first()


	async def get_multi(
		self,
		db: AsyncSession,
		*args,
		offset: int = 0,
		limit: int = 100,
		**kwargs,
	) -> List[ModelType]:
		# Get Multi --

		result = await db.execute(
			select(self.model).\
			filter(*args).\
			filter_by(**kwargs).\
			offset(offset).\
			limit(limit)
		)

		return result.scalars().all()



	def get_multi_sync(
		self,
		db: AsyncSession,
		*args,
		offset: int = 0,
		limit: int = 100,
		**kwargs,
	) -> List[ModelType]:
		# Get Multi Sync --

		result = db.execute(
			select(self.model).\
			filter(*args).\
			filter_by(**kwargs).\
			offset(offset).\
			limit(limit)
		)

		return result.scalars().all()



	async def create(
		self,
		db: AsyncSession,
		obj_in: CreateSchemaType,
	) -> ModelType:
		# Create --

		# obj_in_data = jsonable_encoder(obj_in)

		# ...?
		obj_in_data = obj_in.dict()

		db_obj = self.model(**obj_in_data)

		db.add(db_obj)

		await db.commit()

		return db_obj



	def create_sync(
		self,
		db: AsyncSession,
		obj_in: CreateSchemaType,
	) -> ModelType:
		# Create Sync --

		obj_in_data = obj_in.dict()

		db_obj = self.model(**obj_in_data)

		db.add(db_obj)

		db.commit()

		return db_obj



	async def update(
		self,
		db: AsyncSession,
		obj_in: Union[UpdateSchemaType, Dict[str, Any]],
		db_obj: Optional[ModelType] = None,
		**kwargs,
	) -> Optional[ModelType]:
		# Update --

		db_obj = db_obj or await self.get(session, **kwargs)

		if db_obj is not None:

			# ...? 
			obj_data = jsonable_encoder(db_obj.as_dict())

			if isinstance(obj_in, dict):
				update_data = obj_in
			else:
				update_data = obj_in.dict(
					exclude_unset=True,
				)
			for field in obj_data:
				if field in update_data:
					setattr(
						db_obj,
						field,
						update_data[field],
					)

			db.add(db_obj)

			await db.commit()

		return db_obj



	def update_sync(
		self,
		db: AsyncSession,
		obj_in: Union[UpdateSchemaType, Dict[str, Any]],
		db_obj: Optional[ModelType] = None,
		**kwargs,
	) -> Optional[ModelType]:
		# Update Sync --

		db_obj = db_obj or self.get_sync(session, **kwargs)

		if db_obj is not None:

			# ...? 
			obj_data = jsonable_encoder(db_obj.as_dict())

			if isinstance(obj_in, dict):
				update_data = obj_in
			else:
				update_data = obj_in.dict(
					exclude_unset=True,
				)
			for field in obj_data:
				if field in update_data:
					setattr(
						db_obj,
						field,
						update_data[field],
					)

			db.add(db_obj)

			db.commit()

		return db_obj



	async def delete(
		self,
		db: AsyncSession,
		db_obj: Optional[ModelType] = None,
		**kwargs,
	) -> ModelType:
		# Delete --

		# Explain ... ?
		db_obj = db_obj or await self.get(
			db,
			**kwargs,
		)

		await db.delete(db_obj)
		await db.commit()

		return db_obj



	def delete_sync(
		self,
		db: AsyncSession,
		db_obj: Optional[ModelType] = None,
		**kwargs,
	) -> ModelType:
		# Delete Sync --

		# Explain ... ?
		db_obj = db_obj or self.get_sync(
			db,
			**kwargs,
		)

		db.delete(db_obj)
		db.commit()

		return db_obj






