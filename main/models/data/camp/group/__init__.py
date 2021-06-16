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



class CampGroupModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camp_groups'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	camp = relationship(
		'CampModel',
		back_populates='groups',
		uselist=False,
	)
	camp_id = Column(Integer, ForeignKey('camps.id'))


	instances = relationship(
		'CampGroupInstanceModel',
		back_populates='camp_group',
		lazy='selectin',
		cascade='delete',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}
	
