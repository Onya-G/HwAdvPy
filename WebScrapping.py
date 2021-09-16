import requests
from bs4 import BeautifulSoup as BS

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

responce = requests.get('https://habr.com/ru/all/')
responce.raise_for_status()
soup = BS(responce.text, 'html.parser')
posts = soup.find_all('article', class_='tm-articles-list__item')

for post in posts:
    post_title = post.find('a', class_='tm-article-snippet__title-link')
    link = f"https://habr.com{post_title.attrs.get('href')}"
    res_article = requests.get(link)
    soup_article = BS(res_article.text, 'html.parser')
    article = soup_article.find('div', id="post-content-body")
    if set(KEYWORDS) & set(post.text.lower().split(' ')) or set(KEYWORDS) & set(article.text.lower().split(' ')):
        post_time = post.find('time')
        print(f"{post_time.attrs.get('title')}, {post_title.text}, https://habr.com{post_title.attrs.get('href')}")
