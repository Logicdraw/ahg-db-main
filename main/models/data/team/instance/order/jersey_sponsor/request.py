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



class TeamInstanceJerseySponsorOrderRequestModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_sponsor_order_requests'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_jersey_sponsor_order_requests',
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	# Optional ... ???? --

	# Let us think about this !!

	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_jersey_sponsor_order_requests',
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id')
	)



	team_instance_jersey_sponsor_orders_sc = relationship(
		'TeamInstanceJerseySponsorOrderModel',
		back_populates='team_instance_jersey_sponsor_order_requests',
	)

	team_instance_jersey_sponsor_order_id = Column(
		Integer,
		ForeignKey('team_instance_jersey_sponsor_orders.id')
	)



	player_full_name = Column(
		String,
		index=True,
	)

	name = Column(
		String,
		index=True,
	)

	amount = Column(
		Float,
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


