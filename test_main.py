from pyfile_parser import *


def test_imports():
    assert check_imports(get_lines('sample_app.py')) is True

def test_responses():
    i_lines = [(i, line) for i, line in enumerate(get_lines('sample_app.py'))]
    assert get_responses(i_lines) == ["return 'Hello, World!'"]
