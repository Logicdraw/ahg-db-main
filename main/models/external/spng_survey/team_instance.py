from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.models._base.spng_survey import SpngSurveyBaseModel



from main.config import settings




class SpngSurveyTeamInstanceModel(
	SpngSurveyBaseModel,
	ResourceMixin,
):
	# -- Team
	__tablename__ = 'spng_survey_team_instances'


	id = Column(
		Integer,
		ForeignKey('spng_surveys.id'),
		primary_key=True,
		autoincrement=True,
	)


	# default_team_instance = relationship(
	# 	'TeamInstanceModel',
	# 	uselist=False,
	# )
	# default_team_instance_id = Column(
	# 	Integer,
	# 	ForeignKey('team_instances.id'),
	# )


	# registrations --
	team_instance_registrations = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='spng_survey_team_instances_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
		'eager_defaults': True,
	}



