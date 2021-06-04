from lib.util_datetime import tzware_datetime


from datetime import (
	datetime,
	timezone,
)

import pytz

import timeago


from sqlalchemy import (
	DateTime,
	Column,
)


from sqlalchemy.types import TypeDecorator




class AwareDateTime(TypeDecorator):
	"""
	A DateTime type which can only store tz-aware DateTimes.

	Source:
		https://gist.github.com/inklesspen/90b554c864b99340747e
	"""

	impl = DateTime(timezone=True)


	def process_bind_param(self, value, dialect):

		if isinstance(value, datetime) and value.tzinfo is None:
			raise ValueError('{!r} must be TZ-aware'.format(value))

		return value


	def __repr__(self):
		return 'AwareDateTime()'




class ResourceMixin:
	"""
	Keep track when records are created and updated, also - url strings
	"""

	created_on = Column(AwareDateTime(),
							default=tzware_datetime,)

	updated_on = Column(AwareDateTime(),
							default=tzware_datetime,
							onupdate=tzware_datetime,)



