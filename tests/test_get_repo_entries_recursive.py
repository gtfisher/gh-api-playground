from requests_get_repo import get_repo_entries
from requests_get_repo_recursive import get_repo_entries_recursive
import requests
import requests_mock

import json


def test_get_repo_entries_recursive():
    owner = "chaosiq"
    repo = "rtk-notebooks"
    # owner = "chaosiq"
    # repo = "rtk-notebooks"

    result = get_repo_entries_recursive(repo, owner)
    # print(result)
    print("******************** \n \n")
    print(json.dumps(result, indent=4, sort_keys=True))
    print("******************** \n \n")
