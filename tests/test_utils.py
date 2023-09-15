import json
import unittest

from langchain.schema import Document

from utils import transform_source_docs

mock_result = {
    "source_documents": [],
    "result": "here's a response!"
}

mock_result_with_docs = {
    "source_documents": [Document(
        page_content='some page content',
        metadata={'URL': 'url',
                  'doc_id': 'doc_id',
                  'document_id': 'document_id',
                  'node_info': '{"start": 0, "end": 504, "_node_type": "1"}',
                  'page_id': 'page_id',
                  'ref_doc_id': 'ref_doc_id',
                  'relationships': '{"1": "relationship_id"}',
                  'title': 'A page title here!'})],
    "result": "here's a response!"
}


class TestUtils(unittest.TestCase):

    def test_transform_source_docs(self):
        response_transformed = transform_source_docs(mock_result)
        self.assertIn("here's a response!", response_transformed)
        self.assertIn('"sources": []', response_transformed)
        json.loads(response_transformed)

    def test_transform_source_docs_with_content(self):
        response_transformed = transform_source_docs(mock_result_with_docs)
        self.assertIn("here's a response!", response_transformed)
        self.assertIn('A page title here', response_transformed)
        response = json.loads(response_transformed)
        self.assertEqual(1, len(response['sources']))


if __name__ == '__main__':
    unittest.main()
