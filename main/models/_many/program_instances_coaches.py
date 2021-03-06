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




class ProgramInstancesCoachesModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_instances_coaches'


	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
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



	program_instances_sc = relationship(
		'ProgramInstanceModel',
		back_populates='program_instances_coaches',
	)

	coaches_sc = relationship(
		'CoachModel',
		back_populates='program_instances_coaches',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


