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



class TeamInstanceTracksuitOrderModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_tracksuit_orders'

	id = Column(
		Integer,
		primary_key=True,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_tracksuit_orders',
		uselist=False,
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)



	# Optional ...
	coach_full_name = Column(
		String(120),
	)


	jacket_size = Column(
		String(50),
	)

	pants_size = Column(
		String(50),
	)



	team_instance_tracksuit_order_requests = relationship(
		'TeamInstanceTracksuitOrderRequestModel',
		back_populates='team_instance_tracksuit_orders_sc',
		lazy='selectin',
	)


	team_instance_tracksuit_order_updates = relationship(
		'TeamInstanceTracksuitOrderUpdateModel',
		back_populates='team_instance_tracksuit_orders_sc',
		lazy='selectin',
	)


	# team_instance_tracksuit_order_updates = None


	__mapper_args__ = {
		'eager_defaults': True,
	}


