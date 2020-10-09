import requests
import simplejson as json
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '')
owner = "chaosiq"
repo = "rtk-notebooksxxxx"

headers = {"Authorization": f"Bearer {token}"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        print ("result 200")
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

query2 = f"""
 {{
  repository(name: "{repo}", owner: "{owner}") {{
    object(expression: "master:") {{
      ... on Tree {{
        entries {{
          name
        }}
      }}
    }}

  }}
}}
"""


result = run_query(query2)  # Execute the query
if "errors" in result:
    print("Errors in result")
    print(result['errors'][0]['message'])
else:
    print(json.dumps(result["data"]["repository"]["object"]["entries"]))
