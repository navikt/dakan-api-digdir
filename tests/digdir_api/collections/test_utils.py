import os
import unittest

from unittest import mock

from datacatalogtordf import URI, Location
from digdir_api.collections import utils
from digdir_api.collections.utils import create_language, create_access_rights, create_location, create_format

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

    def test_create_language_multiple(self):
        languages = ["Norsk", "English"]
        languages_out = create_language(languages)
        self.assertNotIsInstance(languages_out, str)
        self.assertIsInstance(languages_out, list)
        self.assertEqual(languages, languages_out)

    def test_create_language_single(self):
        language = "Norsk"
        languages_out = create_language(language)
        self.assertNotIsInstance(languages_out, str)
        self.assertIsInstance(languages_out, list)
        self.assertEqual([language], languages_out)

    def test_create_access_rights_opendata(self):
        inputs = ["open", "opendata", "åpne data"]
        expected_out = URI("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
        for input_access in inputs:
            output = create_access_rights(input_access)
            self.assertEqual(expected_out, output)

    def test_create_location(self):
        expected_location = Location()
        expected_location.identifier = URI("http://sws.geonames.org/3144096/")

        countries = ["Norge", "Norway"]
        for country in countries:
            location = create_location(country)
            self.assertEqual(expected_location.identifier, location.identifier)

    def test_create_format_csv(self):
        inputs = ["csv", "CSV"]
        for input_format in inputs:
            self.assertEqual("text/csv", create_format(input_format))

    def test_create_format_not_csv(self):
        input_format = "application/x.wfs"
        self.assertEqual("application/x.wfs", create_format(input_format))
