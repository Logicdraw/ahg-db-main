from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class TeamInstancesCoachesModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances_coaches'
	
	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
		primary_key=True,
	)
	
	coach_id = Column(
		Integer,
		ForeignKey('coaches.id'),
		primary_key=True,
	)


	role = Column(
		String,
	)


	is_parent_coach = Column(
		Boolean,
		default=False,
	)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instances_coaches',
	)

	coaches_sc = relationship(
		'CoachModel',
		back_populates='team_instances_coaches',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


