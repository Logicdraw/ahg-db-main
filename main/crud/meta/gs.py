from typing import (
	Any,
	Dict,
	Optional,
	Union,
)


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession



from main.crud.base import CRUDBase


from main.database.base import GSMetaModel

from main.schemas.meta.gs import (
	GSMetaSchemaCreate,
	GSMetaSchemaUpdate,
)


from main.security import (
	encode_token,
	token_decoded,
)




class GSNoInstanceError(Exception):
	pass




class CRUDGSMeta(CRUDBase[
		GSMetaModel,
		GSMetaSchemaCreate,
		GSMetaSchemaUpdate,
	]):


	async def get_inst(
		self,
		db: AsyncSession,
	) -> Optional[GSMetaModel]:
		# --

		result = await db.execute(
			select(GSMetaModel)
		)

		inst = result.scalars().first()

		if not inst:
			raise GSNoInstanceError('Not found!')

		return inst


	def get_inst_sync(
		self,
		db: AsyncSession,
	) -> Optional[GSMetaModel]:
		# --

		result = db.execute(
			select(GSMetaModel)
		)

		inst = result.scalars().first()

		if not inst:
			raise GSNoInstanceError('Not found!')

		return inst


	async def get_access_token_decoded(
		self,
		db: AsyncSession,
	) -> Optional[GSMetaModel]:
		# --

		inst = await self.get_inst_(db=db)

		return token_decoded(inst.access_token_encoded)


	def get_access_token_decoded_sync(
		self,
		db: AsyncSession,
	) -> Optional[GSMetaModel]:
		# --

		inst = self.get_inst_sync(db=db)

		return token_decoded(inst.access_token_encoded)


	async def create(
		self,
		db: AsyncSession,
		*,
		obj_in: GSMetaSchemaCreate,
	) -> GSMetaModel:
		# Create --

		db_obj = GSMetaModel(
			access_token_encoded=encode_token(obj_in.access_token),
		)

		db.add(db_obj)

		await db.commit()

		return db_obj


	def create_sync(
		self,
		db: AsyncSession,
		*,
		obj_in: GSMetaSchemaCreate,
	) -> GSMetaModel:
		# Create Sync --

		db_obj = GSMetaModel(
			access_token_encoded=encode_token(obj_in.access_token),
		)

		db.add(db_obj)

		db.commit()

		return db_obj



	async def update(
		self,
		db: AsyncSession,
		*,
		db_obj: GSMetaModel,
		obj_in: Union[GSMetaSchemaUpdate, Dict[str, Any]],
	) -> GSMetaModel:
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
		db_obj: GSMetaModel,
		obj_in: Union[GSMetaSchemaUpdate, Dict[str, Any]],
	) -> GSMetaModel:
		# Update Sync --

		if isinstance(obj_in, dict):
			update_data = obj_in
		else:
			update_data = obj_in.dict(exclude_unset=True)

		try:
			if update_data['access_token']:
				access_token_encoded = encode_token(update_data['access_token'])
				del update_data['access_token']
				update_data['access_token_encoded'] = access_token_encoded
		except KeyError:
			pass


		result = super().\
					update_sync(
						db=db,
						db_obj=db_obj,
						obj_in=update_data,
					)

		return result




gs_meta_crud = CRUDGSMeta(GSMetaModel)



