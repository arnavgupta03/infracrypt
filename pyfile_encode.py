"""Encode flask responses in python file."""
def check_response_type(response) -> str:
    """Return the type of the response"""
    if isinstance(response, str):
        return 'string'
    if isinstance(response, dict):
        return 'json'
    if isinstance(response, int):
        return 'integer'
    return 'unknown'
