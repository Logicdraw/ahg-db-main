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



class TeamInstanceTracksuitOrderRequestModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_tracksuit_order_requests'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_tracksuit_order_requests',
		uselist=False,
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	team_instance_tracksuit_orders_sc = relationship(
		'TeamInstanceTracksuitOrderModel',
		back_populates='team_instance_tracksuit_order_requests',
		uselist=False,
	)

	team_instance_tracksuit_order_id = Column(
		Integer,
		ForeignKey('team_instance_tracksuit_orders.id')
	)



	jacket_size = Column(
		String(50),
	)

	pants_size = Column(
		String(50),
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


	rejection_reason = Column(
		String,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}



# Merge requests ??


