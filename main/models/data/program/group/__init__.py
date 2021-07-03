from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ProgramGroupModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_groups'

	id = Column(
		Integer,
		primary_key=True,
	)


	name = Column(
		String,
	)


	programs_sc = relationship(
		'ProgramModel',
		back_populates='program_groups',
		uselist=False,
	)

	program_id = Column(
		Integer,
		ForeignKey('programs.id'),
	)


	program_group_instances = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_groups_sc',
		lazy='selectin',
		cascade='delete',
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}


	