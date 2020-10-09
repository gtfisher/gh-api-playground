import requests
import simplejson as json
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '')
owner = "chaosiq"
repo = "rtk-notebooks"
filename = "connect-to-reliability-toolkit.ipynb"

headers = {"Authorization": f"Bearer {token}"}

print (headers)


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

query = f"""
 {{
  repository(name: "{repo}", owner: "{owner}") {{
     object(expression: "master:{filename}") {{
      ... on Blob {{
        text
      }}
    }}
    }}

}}
"""


result = run_query(query)  # Execute the query
#print(json.dumps(result))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(json.dumps(result["data"]["repository"]["object"]["text"]))

