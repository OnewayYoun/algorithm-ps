pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
#pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"http://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"http://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
word = 'blind'

#0muzi0muzi0
'''
a = <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta property="og:url" content="https://a.com"/>
</head>
<body>
Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit.
<a href="https://b.com"> Link to b </a>
</body>
</html>
'''

'''
b = <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta property="og:url" content="https://b.com"/>
</head>
<body>
Suspendisse potenti. Vivamus venenatis tellus non turpis bibendum,
<a href="https://a.com"> Link to a </a>
blind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.
<a href="https://c.com"> Link to c </a>
</body>
</html>
'''

'''
c = 
<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta property="og:url" content="https://c.com"/>
</head>  
<body>
Ut condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind
<a href="https://a.com"> Link to a </a>
</body>
</html>
'''
import re

def solution(word, pages):
    scores = []

    for i in pages:
        #전방 후방탐색 이용해서
        #test = '0muzi0muzi0', word = 'muzi' 이런 경우 처리
        basic = len(re.findall('(?<=[^a-z])' + word.lower() + '(?=[^a-z])', i.lower()))
        ext_link = i.lower().count('</a>')
        # basic / ext_link 에서 ext_link 가 0일 경우 예외처리해서 오류 방지
        if ext_link != 0:
            link = float(basic / ext_link)
        else:
            link = 0
        content = re.findall('(?<=<meta property="og:url" content=")https.+?(?="/ ?>)', i)
        content = [] if not content else content[0]
        ext_link_list = re.findall('(?<=<a href=")https.+?(?=">)', i)
        scores.append((basic, link, content, ext_link_list))

    answer = []
    for i in scores:
        score = i[0]
        url = i[2]
        for j in range(len(scores)):
            if url in scores[j][3]:
                score += scores[j][1]
        answer.append(score)

    print(scores)
    print(answer)

    return answer.index(max(answer))

print(solution(word, pages))
