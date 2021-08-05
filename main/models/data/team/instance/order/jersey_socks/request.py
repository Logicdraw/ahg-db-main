from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
	Text,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class TeamInstanceJerseySocksOrderRequestModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_socks_order_requests'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_jersey_socks_order_requests',
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	# Optional ... ???? --

	# Let us think about this !!

	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_jersey_socks_order_requests',
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id')
	)



	team_instance_jersey_socks_orders_sc = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_jersey_socks_order_requests',
	)

	team_instance_jersey_socks_order_id = Column(
		Integer,
		ForeignKey('team_instance_jersey_socks_orders.id')
	)


	# optional
	player_full_name = Column(
		String,
	)



	jersey_number = Column(
		Integer,
	)

	# unlimited
	jersey_size = Column(
		String,
	)


	socks_size = Column(
		String,
	)



	details = Column(
		Text,
	)


	approved = Column(
		Boolean,
	)

	rejected = Column(
		Boolean,
	)


	rejected_reason = Column(
		String,
	)


	# auto calculated way of determining if awaiting approval ... ?


	__mapper_args__ = {
		'eager_defaults': True,
	}



# Merge requests ??


