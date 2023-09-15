import sys
from datetime import datetime

from accuracy_test import accuracy_test
from logger import create_sheet_in_folder

SHARED_FOLDER_ID = '1O2TcHSz8UhSSJoRzvP7QHhnSLVurY5cC'


def ask_questions(question_file_name, questions):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    sheet_name = "{file_name}-{ts}".format(file_name=question_file_name.replace('.', '_'), ts=timestamp)
    sheet_id = create_sheet_in_folder(sheet_name, folder_id=SHARED_FOLDER_ID, sheet_range='Sheet1', sheet_data=[
        [
            'Timestamp(UTC)',
            'Session id',
            'Question',
            'Answer',
            'Sources',
            'Error Message',
            'Accuracy(1 - 5 where 5 is the best)',
            'Comments'
        ]
    ])
    for question in questions:
        try:
            if not question.strip().startswith('#'):
                accuracy_test(sheet_id, question.strip())
        except ValueError as e:
            print(f"Error when asking question {question.strip()}: str(e))")


if __name__ == "__main__":
    question_file = open(sys.argv[1], 'r')
    questions = question_file.readlines()
    ask_questions(question_file.name, questions)
