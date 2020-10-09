from requests_get_repo import get_repo_entries
from requests_get_repo_recursive import get_repo_entries_recursive
import requests
import requests_mock

import json


def test_get_repo_entries():
    result = get_repo_entries()
    # entries = get_entries(result)
    print(result)
