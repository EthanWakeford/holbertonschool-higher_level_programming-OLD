#!/usr/bin/python3
"""reads from a webpage."""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
        print(html)
