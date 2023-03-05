"""Tests for overall functionality."""
import os
import pytest
from infracrypt.pyfile_parser import check_imports, get_lines, get_responses, parse_and_return_responses
from infracrypt.pyfile_encode import get_encryption_key, encrypt_single_response, decrypt_single_response

def test_imports():
    """Test that the check_imports function correctly checks for import of flask"""
    assert check_imports(get_lines(os.path.abspath('./tests/sample_app.py'))) is True

def test_responses():
    """Test that the get_responses function returns the correct responses"""
    i_lines = list(enumerate(get_lines(os.path.abspath('./tests/sample_app.py'))))
    assert get_responses(i_lines) == [
        "return 'Hello, World!'",
        "return {'test_response': 'This is a test'}",
        "return 123",
        "return [1, 2, 3]"
    ]

def test_parse_and_return_responses():
    """Test that the parse_and_return_responses function returns the correct responses"""
    assert parse_and_return_responses(os.path.abspath('./tests/sample_app.py')) == [
        "return 'Hello, World!'",
        "return {'test_response': 'This is a test'}",
        "return 123",
        "return [1, 2, 3]"
    ]

@pytest.mark.skip(reason="no way of getting key without hardware")
def test_get_encoding_key():
    """Test to get the encoding key correctly"""
    key = get_encryption_key()
    print(key)
    assert key is not None

@pytest.mark.skip(reason="no way of getting key without hardware")
def test_encrypt_single_response():
    """Test that the encrypt_single_response function returns the correct response"""
    assert decrypt_single_response(encrypt_single_response(
        "return 'Hello, World!'"
    )) == "return 'Hello, World!'"
