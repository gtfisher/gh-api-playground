# Github api play ground repo

A playground project for the GH api, was using to do some demo work around
pulling notebook files and makrdoewn files from a repo.


## Query Strings

Query string to get text for a file, in a folder, on a branch

```bash
query {
  repository(owner: "chaosiq", name: "rtk-notebooks") {
    object(expression: "master:kubernetes-kill-pod/README.md") {
      ... on Blob {
        text
      }
    }
  }
}
```

Query string to get get file list with subdirs

```bash
query {
          repository(name: "rtk-notebooks", owner: "chaosiq") {
            object(expression: "issue#2:") {
              ... on Tree {
                entries {
                  name
                  object {
                    ... on Tree {
                      entries {
                        name
                        object {
                          ... on Tree {
                            entries {
                              name
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }

          }
        }
  ```

  Can run with:

  GITHUB_TOKEN="<API_TOKEN>" pytest -q -s tests/test_get_repo_entries_recursive.py
  GITHUB_TOKEN="<API_TOKEN>" python requests_get_repo_recursive.py
