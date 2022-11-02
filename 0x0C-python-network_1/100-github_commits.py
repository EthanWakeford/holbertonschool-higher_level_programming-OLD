#!/usr/bin/python3
"""gets the last 10 commits from repo"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]

    payload = {}
    payload['per_page'] = 10
    payload['page'] = 1

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(repo, owner), params=payload)

    commit_list = []

    for commit in r.json():
        sha = commit.get("sha")
        author = commit.get("commit", {}).get("author", {}).get("name")
        commit_list.append("{}: {}".format(sha, author))

    for i in commit_list:
        print(i)
