import os
import unittest

from unittest import mock
from digdir_api.collections.apis import catalog
from tests.digdir_api.collections.test_resources.common import ES_INDEX_ENDPOINT,  PUBLISHER, COLLECTION_IDENTIFIER,\
    API_CONCEPT_TYPE, CATALOG_HOMEPAGE
from tests.digdir_api.collections.test_resources.mock_es_index import mock_requests_post
from tests.digdir_api.collections.test_resources.api_rdf import API_RDF


class TestCollection(unittest.TestCase):

    def setUp(self):
        os.environ["ES_INDEX_ENDPOINT"] = ES_INDEX_ENDPOINT
        os.environ["COLLECTION_IDENTIFIER"] = COLLECTION_IDENTIFIER
        os.environ["PUBLISHER"] = PUBLISHER
        os.environ["API_CONCEPT_TYPE"] = API_CONCEPT_TYPE
        os.environ["CATALOG_HOMEPAGE"] = CATALOG_HOMEPAGE

    @mock.patch("requests.post", side_effect=mock_requests_post)
    def test_create_collection(self, mock_post):
        api_rdf = catalog.create_catalog()
        self.assertEqual(API_RDF, api_rdf)

