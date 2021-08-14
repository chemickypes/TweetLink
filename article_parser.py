from bs4 import BeautifulSoup as BS
import requests


def get_raw_data(url):
    page = requests.get(url)
    soup = BS(page.content, "html.parser")
    title = soup.find('title').text
    lang = soup.find('html')['lang']
    text_body = soup.find('body').text.replace("\n", " ").replace("\xa0", " ")
    return title, lang, text_body


def parse_article(url):
    """
    this method get a link (url) adn generate a dict with:
    - short url
    - original url
    - list of hashtags
    - brief description
    """
    print(get_raw_data(url))
    pass


if __name__ == '__main__':
    parse_article('https://www.coramdeo.it/articoli/5-motivi-per-cui-i-bambini-fanno-parte-del-culto-principale/')
