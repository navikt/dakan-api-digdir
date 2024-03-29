import requests

from tests.digdir_api.collections.test_resources.common import ES_INDEX_ENDPOINT
from tests.digdir_api.collections.test_resources.common import API_CONCEPT_TYPE
from tests.digdir_api.collections.test_resources.term_response_json import TERM_JSON


class MockEsIndexResponse:
    def __init__(self, response_json, status_code):
        self._response_json = response_json
        self._status_code = status_code

    @property
    def status_code(self):
        return self._status_code

    def json(self):
        return self._response_json

    def raise_for_status(self):
        if self._status_code >= 400:
            raise requests.exceptions.HTTPError(self._status_code)


# Mock method used to replace requests.post
def mock_requests_post(url: str, json: dict):
    if url == ES_INDEX_ENDPOINT:
        return MockEsIndexResponse(TERM_JSON, 200)
    else:
        return MockEsIndexResponse(None, 404)
