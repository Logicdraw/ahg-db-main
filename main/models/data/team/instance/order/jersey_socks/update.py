from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class TeamInstanceJerseySocksOrderUpdateModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_socks_order_updates'

	id = Column(
		Integer,
		primary_key=True,
	)



	team_instance_jersey_socks_orders_sc = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_jersey_socks_order_updates',
		uselist=False,
	)

	team_instance_jersey_socks_order_id = Column(
		Integer,
		ForeignKey('team_instance_jersey_socks_orders.id')
	)



	new_player_full_name = Column(
		String,
	)


	new_jersey_number = Column(
		Integer,
	)

	new_jersey_size = Column(
		String,
	)


	new_socks_size = Column(
		String,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}






