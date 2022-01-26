#Python program to access and print a URL's content to the console.

from http.client import HTTPConnection
conn = HTTPConnection('www.google.com')
conn.request('GET','/')
result = conn.getresponse()
content = result.read()
print(content)