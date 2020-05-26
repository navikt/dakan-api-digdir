import os
import unittest

from unittest import mock

from digdir_api.collections import utils
from tests.digdir_api.collections.test_resources.common import TERM_CONCEPT_TYPE, ES_INDEX_ENDPOINT, \
    DATASET_CONCEPT_TYPE
from tests.digdir_api.collections.test_resources.dataset_response_json import DATASET_JSON
from tests.digdir_api.collections.test_resources.mock_es_index import mock_requests_post
from tests.digdir_api.collections.test_resources.term_response_json import TERM_JSON


class TestUtils(unittest.TestCase):

    def setUp(self):
        os.environ["ES_INDEX_ENDPOINT"] = ES_INDEX_ENDPOINT

    def tearDown(self):
        del os.environ["ES_INDEX_ENDPOINT"]

    @mock.patch("requests.post", side_effect=mock_requests_post)
    def test_get_es_docs_of_type(self, mock_post):
        doc_types = [(TERM_CONCEPT_TYPE, TERM_JSON), (DATASET_CONCEPT_TYPE, DATASET_JSON)]
        for doc_type in doc_types:
            with self.subTest(msg=f"Testing doc_type: {doc_type[0]}", _input=doc_type[0]):
                es_doc = utils.get_es_docs_of_type(doc_type[0], 10000)
                self.assertEqual(es_doc, doc_type[1]["hits"]["hits"])

    def test_remove_new_line_valid(self):
        string = "test\r\ntest\r\n"
        expected_washed_string = "testtest"
        washed_string = utils.remove_new_line(string)
        self.assertEqual(washed_string, expected_washed_string)

    def test_remove_new_line_None(self):
        string = None
        expected_washed_string = ""
        washed_string = utils.remove_new_line(string)
        self.assertEqual(washed_string, expected_washed_string)
