# An example to get the remaining rate limit using the Github GraphQL API.

import requests
import simplejson as json

headers = {"Authorization": "Bearer 7ac45009533f135a20c833b4062c7c66026e311a"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""

result = run_query(query) # Execute the query
# print (result)
remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
# print("Remaining rate limit - {}".format(remaining_rate_limit))

repo = "jupyter-notebooks"
owner = "gtfisher"

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
print(json.dumps(result["data"]["repository"]["object"]["entries"]))
