import logging
from os import path
import requests
from bs4 import BeautifulSoup


def log_decor(function):
    """ Декоратор создает лог-файл с именем функции и записывает в него время вызова,
    имя функции, аргументы, результат и путь к логам"""
    def logged_function(*args, **kwargs):
        log_file_name = f'{function.__name__}.log'
        LOG_FORMAT = "%(asctime)s\n%(message)s"
        logging.basicConfig(level=logging.INFO, filename=log_file_name, format=LOG_FORMAT)
        logger = logging.getLogger()
        result = function(*args, **kwargs)
        logger.info(f"function name: {function.__name__}\narguments: {*args, kwargs}\n\
result: {result}\npath to log: {path.abspath(log_file_name)}\n")
        return result

    return logged_function


@log_decor
def habr_posts(keywords):
    """Функция принимает список ключевых слов и ищет по ним свежие статьи на habr.com
    Выводит дату, заголовок и ссылку на статью
    Возвращает количество найденных статей для записи в лог-файл"""
    article_count = 0
    responce = requests.get('https://habr.com/ru/all/')
    responce.raise_for_status()
    soup = BeautifulSoup(responce.text, 'html.parser')
    posts = soup.find_all('article', class_='tm-articles-list__item')

    for post in posts:
        post_title = post.find('a', class_='tm-article-snippet__title-link')
        link = f"https://habr.com{post_title.attrs.get('href')}"
        res_article = requests.get(link)
        soup_article = BeautifulSoup(res_article.text, 'html.parser')
        article = soup_article.find('div', id="post-content-body")
        if set(keywords) & set(post.text.lower().split(' ')) or set(keywords) & set(article.text.lower().split(' ')):
            article_count += 1
            post_time = post.find('time')
            print(f"{post_time.attrs.get('title')}, {post_title.text}, https://habr.com{post_title.attrs.get('href')}")
    return f'{article_count} articles found'


if __name__ == '__main__':
    habr_posts(['дизайн', 'фото', 'web', 'python'])
