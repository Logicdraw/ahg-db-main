from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class TeamModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'teams'

	id = Column(Integer, primary_key=True)

	name = Column(String, index=True)


	city = Column(String, index=True)

	province = Column(String, index=True)


	gender = Column(String(25), index=True)



	divisions_sc = relationship(
		'DivisionModel',
		back_populates='teams',
		uselist=False,
	)
	division_id = Column(
		Integer,
		ForeignKey('divisions.id'),
	)

	conferences_sc = relationship(
		'ConferenceModel',
		back_populates='teams',
		uselist=False,
	)
	conference_id = Column(
		Integer,
		ForeignKey('conferences.id'),
	)

	leagues_sc = relationship(
		'LeagueModel',
		back_populates='teams',
		uselist=False,
	)
	league_id = Column(
		Integer,
		ForeignKey('leagues.id'),
	)

	seasons_sc = relationship(
		'SeasonModel',
		back_populates='teams',
		uselist=False,
	)
	season_id = Column(
		Integer,
		ForeignKey('seasons.id'),
	)



	team_instances = relationship(
		'TeamInstanceModel',
		back_populates='teams_sc',
		lazy='selectin',
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}
	

