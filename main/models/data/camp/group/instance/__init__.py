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



class CampGroupInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camp_group_instances'

	id = Column(Integer, primary_key=True)


	camp_instances_sc = relationship(
		'CampInstanceModel',
		back_populates='camp_group_instances',
		uselist=False,
	)
	camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
	)


	camp_groups_sc = relationship(
		'CampGroupModel',
		back_populates='camp_group_instances',
		uselist=False,
	)
	camp_group_id = Column(
		Integer,
		ForeignKey('camp_groups.id'),
	)


	camp_instance_registrations = relationship(
		'CampInstanceRegistrationModel',
		back_populates='camp_group_instances_sc',
		lazy='selectin',
	)


	year_start = Column(Integer)

	year_end = Column(Integer)



	__mapper_args__ = {
		'eager_defaults': True,
	}

	

