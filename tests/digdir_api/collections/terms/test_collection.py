import os
import unittest

from unittest import mock
from dakan_api_digdir.collections.terms import collection
from tests.digdir_api.collections.test_resources.common import ES_INDEX_ENDPOINT, TERM_CONCEPT_TYPE, \
    TERM_CONCEPT_CONTACT, TERM_CONCEPT_IDENTIFIER, PUBLISHER
from tests.digdir_api.collections.test_resources.mock_es_index import mock_requests_post
from tests.digdir_api.collections.test_resources.term_rdf import TERMS_RDF


class TestCollection(unittest.TestCase):

    def setUp(self):
        os.environ["ES_INDEX_ENDPOINT"] = ES_INDEX_ENDPOINT
        os.environ["ES_INDEX_ENDPOINT_TERMS"] = ES_INDEX_ENDPOINT
        os.environ["TERM_CONCEPT_TYPE"] = TERM_CONCEPT_TYPE
        os.environ["TERM_CONCEPT_CONTACT"] = TERM_CONCEPT_CONTACT
        os.environ["TERM_CONCEPT_IDENTIFIER"] = TERM_CONCEPT_IDENTIFIER
        os.environ["PUBLISHER"] = PUBLISHER

    @mock.patch("requests.post", side_effect=mock_requests_post)
    def test_create_collection(self, mock_post):
        self.maxDiff = None
        terms_rdf = collection.create_collection()
        self.assertEqual(terms_rdf, TERMS_RDF)
