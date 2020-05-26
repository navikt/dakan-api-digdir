import os
import unittest

from unittest import mock
from digdir_api.collections.terms import collection
from tests.digdir_api.collections.test_resources.common import ES_INDEX_ENDPOINT, TERM_CONCEPT_TYPE, \
    TERM_CONCEPT_CONTACT, TERM_CONCEPT_IDENTIFIER, PUBLISHER, COLLECTION_IDENTIFIER, TERM_COLLECTION_NAME
from tests.digdir_api.collections.test_resources.mock_es_index import mock_requests_post
from tests.digdir_api.collections.test_resources.term_rdf import TERMS_RDF


class TestCollection(unittest.TestCase):

    def setUp(self):
        os.environ["ES_INDEX_ENDPOINT"] = ES_INDEX_ENDPOINT
        os.environ["COLLECTION_IDENTIFIER"] = COLLECTION_IDENTIFIER
        os.environ["TERM_COLLECTION_NAME"] = TERM_COLLECTION_NAME
        os.environ["TERM_CONCEPT_TYPE"] = TERM_CONCEPT_TYPE
        os.environ["TERM_CONCEPT_CONTACT"] = TERM_CONCEPT_CONTACT
        os.environ["TERM_CONCEPT_IDENTIFIER"] = TERM_CONCEPT_IDENTIFIER
        os.environ["PUBLISHER"] = PUBLISHER

    @mock.patch("requests.post", side_effect=mock_requests_post)
    def test_create_collection(self, mock_post):
        terms_rdf = collection.create_collection()
        self.assertEqual(terms_rdf, TERMS_RDF)

