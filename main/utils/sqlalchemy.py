from main.utils.datetime import tzware_datetime


from datetime import (
	datetime,
	timezone,
)

import pytz

import timeago


from sqlalchemy import (
	DateTime,
	Column,
	func,
	text,
)


from sqlalchemy.types import TypeDecorator




class AwareDateTime(TypeDecorator):
	"""
	A DateTime type which can only store tz-aware DateTimes.

	Source:
		https://gist.github.com/inklesspen/90b554c864b99340747e
	"""

	impl = DateTime(timezone=True)


	# To be safe ... (Not an expert...)
	cache_ok = False


	def process_bind_param(self, value, dialect):

		if isinstance(value, datetime) and value.tzinfo is None:
			raise ValueError('{!r} must be TZ-aware'.format(value))

		return value


	def __repr__(self):
		return 'AwareDateTime()'




class ResourceMixin:
	# Keep track when records are created and updated, also - url strings --

	created_on = Column(AwareDateTime(),
							server_default=text("timezone('utc'::text, now())"),)

	updated_on = Column(AwareDateTime(),
							server_default=text("timezone('utc'::text, now())"),
							server_onupdate=text("timezone('utc'::text, now())"),)






