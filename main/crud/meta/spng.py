from typing import (
	Any,
	Dict,
	Optional,
	Union,
)


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.base import CRUDBase


from main.database.base import SpngMetaModel

from main.schemas.meta.spng import (
	SpngMetaSchemaCreate,
	SpngMetaSchemaUpdate,
)


from main.security import (
	encode_token,
	token_decoded,
)




class SpngNoInstanceError(Exception):
	pass




class CRUDSpngMeta(CRUDBase[
		SpngMetaModel,
		SpngMetaSchemaCreate,
		SpngMetaSchemaUpdate,
	]):


	async def get_inst(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		result = await db.execute(
			select(SpngMetaModel)
		)

		inst = result.scalars().first()

		if not inst:
			raise SpngNoInstanceError('Not found!')

		return inst


	def get_inst_sync(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		result = db.execute(
			select(SpngMetaModel)
		)

		inst = result.scalars().first()

		if not inst:
			raise SpngNoInstanceError('Not found!')

		return inst



	async def get_access_token_decoded(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		inst = await self.get_inst(db=db)

		return token_decoded(inst.access_token_encoded)


	def get_access_token_decoded_sync(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		inst = self.get_inst_sync(db=db)

		return token_decoded(inst.access_token_encoded)


	async def get_refresh_token_decoded(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		inst = await self.get_inst(db=db)

		return token_decoded(inst.refresh_token_encoded)


	def get_refresh_token_decoded_sync(
		self,
		db: AsyncSession,
	) -> Optional[SpngMetaModel]:
		# --

		inst = self.get_inst_sync(db=db)

		return token_decoded(inst.refresh_token_encoded)


	async def create(
		self,
		db: AsyncSession,
		*,
		obj_in: SpngMetaSchemaCreate,
	) -> SpngMetaModel:
		# Create --

		db_obj = SpngMetaModel(
			access_token_encoded=encode_token(obj_in.access_token),
			refresh_token_encoded=encode_token(obj_in.refresh_token),
		)

		db.add(db_obj)

		await db.commit()

		return db_obj


	def create_sync(
		self,
		db: AsyncSession,
		*,
		obj_in: SpngMetaSchemaCreate,
	) -> SpngMetaModel:
		# Create Sync --

		db_obj = SpngMetaModel(
			access_token_encoded=encode_token(obj_in.access_token),
			refresh_token_encoded=encode_token(obj_in.refresh_token),
		)

		db.add(db_obj)

		db.commit()

		return db_obj


	async def update(
		self,
		db: AsyncSession,
		*,
		db_obj: SpngMetaModel,
		obj_in: Union[SpngMetaSchemaUpdate, Dict[str, Any]],
	) -> SpngMetaModel:
		# Update --

		if isinstance(obj_in, dict):
			update_data = obj_in
		else:
			update_data = obj_in.dict(exclude_unset=True)

		try:
			if update_data['access_token']:
				access_token_encoded = encode_token(update_data['access_token'])
				del update_data['access_token']
				update_data['access_token_encoded'] = access_token_encoded

			if update_data['refresh_token']:
				refresh_token_encoded = encode_token(update_data['refresh_token'])
				del update_data['refresh_token']
				update_data['refresh_token_encoded'] = refresh_token_encoded
		except KeyError:
			pass


		result = await super().\
						update(
							db=db,
							db_obj=db_obj,
							obj_in=update_data,
						)

		return result


	def update_sync(
		self,
		db: AsyncSession,
		*,
		db_obj: SpngMetaModel,
		obj_in: Union[SpngMetaSchemaUpdate, Dict[str, Any]],
	) -> SpngMetaModel:
		# Update --

		if isinstance(obj_in, dict):
			update_data = obj_in
		else:
			update_data = obj_in.dict(exclude_unset=True)

		try:
			if update_data['access_token']:
				access_token_encoded = encode_token(update_data['access_token'])
				del update_data['access_token']
				update_data['access_token_encoded'] = access_token_encoded

			if update_data['refresh_token']:
				refresh_token_encoded = encode_token(update_data['refresh_token'])
				del update_data['refresh_token']
				update_data['refresh_token_encoded'] = refresh_token_encoded
		except KeyError:
			pass


		result = super().\
					update_sync(
						db=db,
						db_obj=db_obj,
						obj_in=update_data,
					)

		return result




spng_meta_crud = CRUDSpngMeta(SpngMetaModel)



