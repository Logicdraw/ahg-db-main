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


	camps_sc = relationship(
		'CampModel',
		back_populates='camp_groups',
		uselist=False,
	)
	camp_id = Column(Integer, ForeignKey('camps.id'))


	camp_group_instances = relationship(
		'CampGroupInstanceModel',
		back_populates='camp_groups_sc',
		lazy='selectin',
		cascade='delete',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}
	
