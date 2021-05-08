import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from typing import Dict

from fastapi.testclient import TestClient

from app.config.settings import get_settings
settings = get_settings()



def test_root(
	client: TestClient,
) -> None:
	"""
	Test Root
	"""

	resp = client.get(
		'/',
	)
	result = resp.json()
	
	assert resp.status_code == 200

