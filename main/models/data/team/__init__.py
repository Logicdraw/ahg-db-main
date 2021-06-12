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

from lib.util_sqlalchemy import (
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


	GENDERS = OrderedDict([
		('male', 'Male'),
		('female', 'Female'),
		('both', 'Both'),
	])

	gender = Column(Enum(*GENDERS, name='gender_types', native_enum=False), 
					index=True, nullable=True)



	division = relationship(
		'DivisionModel',
		back_populates='teams',
		uselist=False,
	)
	division_id = Column(
		Integer,
		ForeignKey('divisions.id'),
	)

	conference = relationship(
		'ConferenceModel',
		back_populates='teams',
		uselist=False,
	)
	conference_id = Column(
		Integer,
		ForeignKey('conferences.id'),
	)

	league = relationship(
		'LeagueModel',
		back_populates='teams',
		uselist=False,
	)
	league_id = Column(
		Integer,
		ForeignKey('leagues.id'),
	)

	season = relationship(
		'SeasonModel',
		back_populates='teams',
		uselist=False,
	)
	season_id = Column(
		Integer,
		ForeignKey('seasons.id'),
	)



	instances = relationship('TeamInstanceModel', back_populates='team', lazy='selectin')




