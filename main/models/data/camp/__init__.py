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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class CampModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camps'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	camp_instances = relationship(
		'CampInstanceModel',
		back_populates='camps_sc',
		lazy='selectin',
		cascade='delete',
	)

	camp_groups = relationship(
		'CampGroupModel',
		back_populates='camps_sc',
		lazy='selectin',
		cascade='delete',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}

