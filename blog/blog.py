# __author:"Destiny"
# date: 2018/1/15
import re

import requests
from bs4 import BeautifulSoup

from config import setting


def get_first_page():
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            'referer': 'https://blog.wangjian.ltd/'}
    r = requests.get(setting.PASSAGE_URL, headers=head)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        passages = soup.body.content.find(name='div', attrs={'class': 'main'})
        title_url = passages.find_all(name='div', attrs='article-title')
        title = [i.a.string.strip() for i in title_url]
        url = [i.a['href'] for i in title_url]
        content = soup.find_all(name='div', attrs={'class': 'article-content'})
        content = [i.text.strip().replace('\n', '').replace('\r', '').replace('\t', '') for i in content]
        time = passages.find_all(name='small')
        time = [re.search('\d*-\d{1,2}-\d{1,2}', str(i)).group() for i in time]
        count = 0
        articles = {}
        for (i, j, k, l) in zip(title, content, url, time):
            articles[count] = {'title': i, 'content': "%s%s" % (j[:50], '...'), 'url': k, 'time': l, 'id': count}
            count += 1
        return articles


def get_article(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        a = soup.find(name='div', attrs={'class': 'article-content'})
        return str(a)
    else:
        print(r.status_code)
        return False


if __name__ == "__main__":
    # title, content, url, time = get_first_page()
    # count = 0
    # articles = {}
    # for (i, j, k, l) in zip(title, content, url, time):
    #     articles[count] = {'title': i, 'content': content, 'url': url, 'time': time}
    #     count += 1
    # print(articles)

    # count = 0
    # a={}
    # for  i in ['1','2','3']:
    #     a[count]={'num':i}
    #     count += 1
    # print(a)
    print(get_article(''))
    pass
