from github import Github
import os
from pprint import pprint
import simplejson as json
# from ..json import JSONEncoder


token = os.getenv('GITHUB_TOKEN', '7ac45009533f135a20c833b4062c7c66026e311a')
g = Github (token)
repo = g.get_repo("gtfisher/jupyter-notebooks")
contents = repo.get_contents('/')
print(30*'*')
pprint(contents)
print(20*'*')
# pprint(json.dumps({'contents': 'suff'}, cls=JSONEncoder))
pprint(json.dumps(contents))
