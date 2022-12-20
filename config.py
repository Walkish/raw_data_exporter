import ast
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


def get_raw_data_conf() -> Dict:
    """ A rough idea how to use fernet
    https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/"""

    key = os.getenv("FERNET_KEY")
    if not key:
        raise ValueError ("Add FERNET_KEY and try again")
    fernet = Fernet(key)

    with open("raw_data_string.txt", 'rb') as file:
        secret_string = file.read()

    return ast.literal_eval(fernet.decrypt(secret_string).decode())
