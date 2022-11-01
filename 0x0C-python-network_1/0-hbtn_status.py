#!/usr/bin/python3
'''reads from a webpage.'''


if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(f"""Body response:
    - type: {type(page)}
    - content: {page}
    - utf8 content: {page.decode('utf8')}""")
