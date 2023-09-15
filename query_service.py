import json

from agent import Agent
from pinecone_database import get_pinecone_index


class QueryService:

    def __init__(self):
        self.agent = Agent()
        self.vector_database_query_engine = self._create_vector_database_query_engine()

    def _create_query_session(self):
        self.agent = Agent()

    def _create_vector_database_query_engine(self):
        pinecone_index = get_pinecone_index()
        return pinecone_index.as_query_engine()

    def search_vector_database(self, question: str):
        response = self.vector_database_query_engine.query(question)
        return response.response

    def ask_agent(self, question: str):
        try:
            answer = self.agent.query_agent(user_input=question)
            response_formatted = json.loads(answer, strict=False)
        except Exception as e:
            print(f"An error occurred when querying the agent. Error: {e}")
            raise e

        return {"response": response_formatted, }
