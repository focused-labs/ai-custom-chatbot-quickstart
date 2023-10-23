import json
import unittest

from utils import transform_to_json

mock_result = {
    "result": "here's a response!"
}


class TestUtils(unittest.TestCase):

    def test_transform_source_docs(self):
        response_transformed = transform_to_json(mock_result)
        self.assertIn("here's a response!", response_transformed)
        json.loads(response_transformed)


if __name__ == '__main__':
    unittest.main()
