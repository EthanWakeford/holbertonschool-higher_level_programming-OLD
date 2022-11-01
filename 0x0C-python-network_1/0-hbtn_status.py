#!/usr/bin/python3
"""reads from a webpage."""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print(html)
