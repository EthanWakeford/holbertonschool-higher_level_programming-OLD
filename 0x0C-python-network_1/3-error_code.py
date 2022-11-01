#!/usr/bin/python3
"""handles errors"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]

    req = urllib.request.Request(url)
    try: urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)      
