#!/usr/bin/python3
""""""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        info = response.info()
        print(info.get('X-Request-Id'))
