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



class AdultRepModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'adult_reps'

	id = Column(Integer, primary_key=True)


	full_name = Column(String, index=True)

	email = Column(String, unique=True)


	team_instances_adult_reps = relationship(
		'TeamInstancesAdultRepsModel',
		back_populates='adult_reps_sc',
		lazy='selectin',
		cascade='delete',
	)


	users_sc = relationship(
		'UserModel',
		uselist=False,
	)
	user_id = Column(
		Integer,
		ForeignKey('users.id'),
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}
	

