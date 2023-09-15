import json

from agent import Agent
from logger import save_question, save_error


def accuracy_test(spreadsheet_id, question):
    agent = Agent(personality="human")
    try:
        answer = agent.query_agent(question)
        response_formatted = json.loads(answer, strict=False)
        save_question(question=question, answer=response_formatted, sheet_id=spreadsheet_id)
    except Exception as e:
        save_error(question, str(e), spreadsheet_id)
        raise e
