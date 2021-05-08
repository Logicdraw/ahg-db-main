import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from fastapi import FastAPI


from app.config import get_settings
settings = get_settings()


from raven import Client


import os



app = FastAPI(
	title=settings.PROJECT_NAME,
)


if (settings.STAGING or settings.PRODUCTION):
	client_sentry = Client(settings.SENTRY_DSN)



@app.get('/')
async def read_root():
	return {'it is...': 'working!'}



logger.info('FASTAPI APP CREATED!')


