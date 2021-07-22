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



class TeamInstanceTracksuitOrderUpdateModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_tracksuit_order_updates'

	id = Column(
		Integer,
		primary_key=True,
	)



	team_instance_tracksuit_orders_sc = relationship(
		'TeamInstanceTracksuitOrdersModel',
		back_populates='team_instance_tracksuit_order_updates',
		uselist=False,
	)

	team_instance_tracksuit_order_id = Column(
		Integer,
		ForeignKey('team_instance_tracksuit_orders.id')
	)


	# Optional ...
	new_coach_full_name = Column(
		String(120),
	)


	new_jacket_size = Column(
		String(50),
	)

	new_pants_size = Column(
		String(50),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}






