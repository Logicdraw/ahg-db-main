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



class CoachModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'coaches'

	id = Column(Integer, primary_key=True)


	full_name = Column(String, index=True)

	email = Column(String, unique=True)


	team_instances_coaches = relationship(
		'TeamInstancesCoachesModel',
		back_populates='coaches_sc',
		lazy='selectin',
		cascade='delete',
	)

	camp_instances_coaches = relationship(
		'CampInstancesCoachesModel',
		back_populates='coaches_sc',
		lazy='selectin',
		cascade='delete',
	)

	program_instances_coaches = relationship(
		'ProgramInstancesCoachesModel',
		back_populates='coaches_sc',
		lazy='selectin',
		cascade='delete',
	)



	users_sc = relationship(
		'UserModel',
		uselist=False,
	)
	user_id = Column(Integer, ForeignKey('users.id'))



	__mapper_args__ = {
		'eager_defaults': True,
	}
	

