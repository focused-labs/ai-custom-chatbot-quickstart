import json


def output_response(response) -> None:
    if not response:
        print("There's no response.")
    else:
        print(response)
    print("-----")


def is_answer_formatted_in_json(answer):
    try:
        json.loads(answer, strict=False)
        return True
    except ValueError:
        return False


def format_escape_characters(s):
    return s.replace('"', '\\"').replace("\n", "\\n")


def transform_to_json(result):
    formatted_result_string = format_escape_characters(result["result"])
    return f"""
        {{
        "result": "{formatted_result_string}"
        }}"""
