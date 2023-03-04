from pyfile_parser import check_imports


def test_imports():
    assert check_imports('sample_app.py') is True
