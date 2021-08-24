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



class TeamInstanceJerseySponsorOrderModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_sponsor_orders'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_jersey_sponsor_orders',
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_jersey_sponsor_orders',
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id')
	)


	name = Column(
		String,
		index=True,
	)

	amount = Column(
		Float,
	)



	team_instance_jersey_sponsor_order_requests = relationship(
		'TeamInstanceJerseySponsorOrderRequestModel',
		back_populates='team_instance_jersey_sponsor_orders_sc',
		lazy='dynamic',
	)


	team_instance_jersey_sponsor_order_updates = relationship(
		'TeamInstanceJerseySponsorOrderUpdateModel',
		back_populates='team_instance_jersey_sponsor_orders_sc',
		lazy='dynamic',
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}






