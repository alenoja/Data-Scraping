from re import findall

def getEmails(content):
    pattern = '[\w\.]+@[\w\.]+.'
    emails = findall(pattern, content)
    return emails

infile = open('C:\\Users\\aleno\\Desktop\\Spring 2021\\Lab3_Webpage-1.html')
content = infile.read()
infile.close()

print(getEmails(content))