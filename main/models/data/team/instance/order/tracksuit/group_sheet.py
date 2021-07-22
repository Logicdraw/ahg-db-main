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



class TeamInstanceTracksuitOrderGroupSheetModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_tracksuit_order_group_sheets'

	id = Column(
		Integer,
		primary_key=True,
	)

	uuid = Column(
		String(32),
		nullable=False,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_tracksuit_order_group_sheets',
		uselist=False,
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}



# Merge requests ??


