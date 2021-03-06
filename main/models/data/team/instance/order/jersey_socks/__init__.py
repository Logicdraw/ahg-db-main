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



class TeamInstanceJerseySocksOrderModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_socks_orders'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_jersey_socks_orders',
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_jersey_socks_orders',
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id')
	)


	player_full_name = Column(
		String,
	)



	jersey_number = Column(
		Integer,
	)

	jersey_size = Column(
		String,
	)


	socks_size = Column(
		String,
	)



	team_instance_jersey_socks_order_requests = relationship(
		'TeamInstanceJerseySocksOrderRequestModel',
		back_populates='team_instance_jersey_socks_orders_sc',
		lazy='selectin',
	)


	team_instance_jersey_socks_order_updates = relationship(
		'TeamInstanceJerseySocksOrderUpdateModel',
		back_populates='team_instance_jersey_socks_orders_sc',
		lazy='selectin',
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}






