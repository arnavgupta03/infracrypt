from pyfile_parser import check_imports, get_lines, get_responses, parse_and_return_responses


def test_imports():
    assert check_imports(get_lines('sample_app.py')) is True

def test_responses():
    i_lines = [(i, line) for i, line in enumerate(get_lines('sample_app.py'))]
    assert get_responses(i_lines) == ["return 'Hello, World!'", "return {'test_response': 'This is a test'}"]

def test_parse_and_return_responses():
    assert parse_and_return_responses('sample_app.py') == ["return 'Hello, World!'", "return {'test_response': 'This is a test'}"]