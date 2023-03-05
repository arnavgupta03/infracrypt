"""Infracrypt main module."""
import json
import os
import sys
from infracrypt import pyfile_encode, pyfile_parser

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m infracrypt <path to python file>")
        sys.exit(1)
    arg = sys.argv[1]
    responses = pyfile_parser.parse_and_return_responses(os.path.abspath(arg))
    if responses == 'No imports of flask found, file is invalid':
        sys.exit(1)
    encrypted_responses = pyfile_encode.encrypt_responses([response[1][7:] for response in responses])
    with open("encrypted_responses.json", "w") as jsonfile:
        jsonfile.write(json.dumps({"encryptions" : encrypted_responses}))
    # replace the return statements in the file with the encrypted responses
    lines = []
    with open(os.path.abspath(arg), "r") as file:
        lines = file.readlines()
    enc_counter = 0
    with open(os.path.abspath(arg), "w") as file:
        for i, line in enumerate(lines):
            if line.strip().startswith("return"):
                file.write(line.replace(line.strip()[7:], "'{}'".format(encrypted_responses[enc_counter]["response"])))
                enc_counter += 1
            else:
                file.write(line)
    print("File has been rewritten with encryption!")
    print("Encryption data in encrypted_responses.json")
                           