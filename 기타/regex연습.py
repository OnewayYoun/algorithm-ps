import re

a = 'content="https://www.kakaocorp.com"/>'
aa = 'content="https://www.kakaocorp.com"/">'
aaa = 'content="https://www.kakaocorp.kom"/>'


b = 'content="https://www.kakaocorp.com"/>'
c = '<title> 여기는 제목입니다. </title>'
d = '(나는)(윤한길)(입니다)'

v = 'content="://www.kakaocorp.kom"/>'


print(re.findall('(k)(a|o)', aaa))

print(re.findall('content="(.*?)"/>', a))
print(re.findall('"(.*?)"', aa))
print(re.findall('(?<=content=").+?(?="/>)', b))

print(re.findall('<.*?>', c))

print(re.findall('<(.*?)>', c))
print(re.findall('</?(.*?)>', c))

print(re.findall('\((.*?)\)', d))

content = re.findall('(?<=content=").+?(?="/>)', v)
content = [] if not content else content[0]
print(content)


test = '0muzi0muzi0'
word = 'muzi'
basic = re.findall('(?<=[^a-z])' + word.lower() + '(?=[^a-z])', test.lower())
print(basic)
