from github import Github
import os
from pprint import pprint


token = os.getenv('GITHUB_TOKEN', '')
file_path = "ctk-in-notebook.ipynb"
g = Github(token)
repo = g.get_repo("gtfisher/jupyter-notebooks")

file = repo.get_contents(file_path, ref="master")  # Get file from branch
data = file.decoded_content.decode("utf-8")
print("#" * 30)
pprint(file.content)
