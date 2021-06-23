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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class TeamInstancesAdultRepsModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances_adult_reps'
	
	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
		primary_key=True,
	)
	adult_rep_id = Column(
		Integer,
		ForeignKey('adult_reps.id'),
		primary_key=True,
	)


	role = Column(String)


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instances_adult_reps',
		uselist=False,
	)

	adult_reps_sc = relationship(
		'AdultRepModel',
		back_populates='team_instances_adult_reps',
		uselist=False,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


