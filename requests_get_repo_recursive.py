import requests
import simplejson as json
import os

token = os.getenv('GITHUB_TOKEN', '')
owner = "chaosiq"
repo = "rtk-notebooks"

headers = {"Authorization": f"Bearer {token}"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_repo_entries_recursive(repo, owner):

    query2 = f"""
    {{
      repository(name: "{repo}", owner: "{owner}") {{
        object(expression: "master:") {{
                    ... on Tree {{
                      entries {{
                        path
                        object {{
                          ... on Tree {{
                            entries {{
                              path
                              object {{
                                ... on Tree {{
                                  entries {{
                                    path
                                  }}
                                }}
                              }}
                            }}
                          }}
                        }}
                      }}
                    }}
                  }}
        }}
    }}

    """
    result = run_query(query2)  # Execute the query
    print("******************** \n \n")
    print(result)
    print("\n \n ********************")
    return result
    # return json.dumps(result["data"]["repository"]["object"]["entries"])


if __name__ == '__main__':
    get_repo_entries_recursive(repo, owner)
