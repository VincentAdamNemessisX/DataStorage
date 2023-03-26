"""
# File       : zhihuDiscovery.py
# Time       : 3:15 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
# file storage
# txt storage
import requests
from pyquery import PyQuery


# save question to the dict of quests
def save_titles(contents):
    global index
    for t in contents:
        quests[index] = t.text().strip()
        index += 1


# write all questions in quests to file
def write_to_file():
    global quests
    with open('hotQuestions.txt', 'w+') as f:
        for k, i in quests.items():
            f.write(str(k + 1) + ":" + i + "\n")


url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
}
index = 0
# saved class name that used by questions(Under analysis the pages content)
titles_class = ['ExploreRoundtableCard-title', 'ExploreRoundtableCard-questionTitle',
                'ExploreSpecialCard-contentTitle', 'css-1nd7dqm',
                'ExploreCollectionCard-contentTitle']
quests = {}
html = requests.get(url, headers=headers).text
doc = PyQuery(html)
# with open('test.html', 'w+', encoding='utf-8') as f:
# f.write(html)
for i in range(len(titles_class)):
    titles = doc("." + titles_class[i]).items()
    save_titles(titles)
write_to_file()

