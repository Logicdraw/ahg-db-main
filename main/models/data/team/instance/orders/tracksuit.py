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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class TeamInstanceTracksuitOrderModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_tracksuit_orders'

	id = Column(Integer, primary_key=True)


	team_instance = relationship(
		'TeamInstanceModel',
		back_populates='tracksuit_orders',
		uselist=False,
	)
	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	jacket_size = Column(String(50))

	pants_size = Column(String(50))


	__mapper_args__ = {
		'eager_defaults': True,
	}


