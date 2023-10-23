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
    except ValueError as e:
        return False


def format_quotes_in_json(str):
    return str.replace('"', '\\"').replace("\n", "\\n")


def transform_to_json(result):
    formatted_result_string = format_quotes_in_json(result["result"])
    return f"""
        {{
        "result": "{formatted_result_string}"
        }}"""
