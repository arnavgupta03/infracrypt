"""Tests for overall functionality."""
from pyfile_parser import check_imports, get_lines, get_responses, parse_and_return_responses

def test_imports():
    """Test that the check_imports function correctly checks for import of flask"""
    assert check_imports(get_lines('sample_app.py')) is True

def test_responses():
    """Test that the get_responses function returns the correct responses"""
    i_lines = enumerate(get_lines('sample_app.py'))
    assert get_responses(i_lines) == [
        "return 'Hello, World!'",
        "return {'test_response': 'This is a test'}"
    ]

def test_parse_and_return_responses():
    """Test that the parse_and_return_responses function returns the correct responses"""
    assert parse_and_return_responses('sample_app.py') == [
        "return 'Hello, World!'",
        "return {'test_response': 'This is a test'}"
    ]
