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



class CampInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camp_instances'

	id = Column(Integer, primary_key=True)


	camps_sc = relationship(
		'CampModel',
		back_populates='camp_instances',
		uselist=False,
	)
	camp_id = Column(Integer, ForeignKey('camps.id'))



	camp_instance_registrations = relationship(
		'CampInstanceRegistrationModel',
		back_populates='camp_instances_sc',
		lazy='selectin',
	)

	camp_group_instances = relationship(
		'CampGroupInstanceModel',
		back_populates='camp_instances_sc',
		lazy='selectin',
		cascade='delete',
	)

	camp_instances_coaches = relationship(
		'CampInstancesCoachesModel',
		back_populates='camp_instances_sc',
		lazy='selectin',
	)



	year_start = Column(Integer)

	year_end = Column(Integer)


	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)



	__mapper_args__ = {
		'eager_defaults': True,
	}

	


