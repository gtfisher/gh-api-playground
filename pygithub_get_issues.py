from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '...')
g = Github (token)
repo = g.get_repo("chaosiq/product")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))
