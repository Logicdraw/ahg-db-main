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



class ProgramModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'programs'

	id = Column(
		Integer,
		primary_key=True,
	)


	name = Column(
		String,
	)


	program_instances = relationship(
		'ProgramInstanceModel',
		back_populates='programs_sc',
		lazy='selectin',
		cascade='delete',
	)

	program_groups = relationship(
		'ProgramGroupModel',
		back_populates='programs_sc',
		lazy='selectin',
		cascade='delete',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}

