url = "https://example.com.tw"
filename = "test_file"

def func1():
    import urllib
    urllib.urlretrieve(url, filename)

def func2():
    import urllib2

    f = urllib2.urlopen(url)
    data = f.read()
    with open(filename, "wb") as code:
        code.write(data)

def func3():
    import requests

    r = requests.get(url)
    with open(filename, "wb") as code:
        code.write(r.content)