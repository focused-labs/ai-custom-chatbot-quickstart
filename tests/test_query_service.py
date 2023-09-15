import unittest
from unittest.mock import patch, Mock

import query_service
from agent import Agent
from models.question import Question

mock_response = f"""
            {{
                "result": "Here's an answer to a question!",
                "sources": []
            }}"""


def mock_response_func(cls, *args, **kwargs):
    return mock_response


class TestQueryService(unittest.TestCase):
    @patch.object(Agent, 'query_agent', mock_response_func)
    @patch("conversation_repository.create_conversation")
    def test_query_service_query_calls_repo_to_log(self, create_convo_repo: Mock):
        under_test = query_service.QueryService()
        q = Question(text="Hello question!", session_id="2ddc72f3-b04d-4516-ac80-cff3619eccd4", role="human")
        under_test.query(
            question=q)
        create_convo_repo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
