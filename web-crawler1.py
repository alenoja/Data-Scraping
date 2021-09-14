from re import findall
from urllib.request import urlopen
from collections import OrderedDict


def getContent(url):
    content = urlopen(url).read().decode()
    pattern = '[\w\.]+@[\w\.]+.'
    emails = findall(pattern, content)
    return emails

url = 'https://www.uta.edu/academics/schools-colleges/business/departments/information-systems-and-operations-management '

print(getContent(url))
