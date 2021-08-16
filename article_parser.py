from bs4 import BeautifulSoup as BS
import requests
import re
import string
import nltk

import secrets
from utils import dict_from_json

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from collections import Counter

english_stopwords = stopwords.words("english")
italian_stopwords = stopwords.words("italian")
italian_stopwords.append('mai')


def get_raw_data_from(url):
    page = requests.get(url)
    soup = BS(page.content, "html.parser")
    title = soup.find('title').text
    lang = soup.find('html')['lang']
    text_body = re.sub(r"\s+", " ", soup.find('body').text.strip())
    return title, lang, text_body


def remove_punctuation(from_text):
    return from_text.translate(str.maketrans('', '', string.punctuation + "’“»«–—”"))


def clean_analysable_text(raw_text, lang):
    """
    this method get complete text and return a list of words without stopwords according the lang
    :param raw_text: complete text
    :param lang: lang of the text (it or en, now)
    :return: list of words
    """
    text_tokens = word_tokenize(remove_punctuation(raw_text).lower())
    list_of_sw = english_stopwords if 'en' in lang else italian_stopwords
    return [word for word in text_tokens if not word in list_of_sw]


def short_link_of(url):
    s = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(secrets.cuttly_api_key, url))
    return dict_from_json(s.text)['url']['shortLink']


def parse_article(url):
    """
    this method get a link (url) adn generate a dict with:
    - short url
    - original url
    - list of hashtags
    - brief description
    """
    title, lang, text_body = get_raw_data_from(url)
    clean_text = clean_analysable_text(f"{title} {text_body}", lang)
    hashtags = [f"#{i[0]}" for i in Counter(clean_text).most_common()[:4]]
    short_url = short_link_of(url)
    print(short_url)
    pass


if __name__ == '__main__':
    parse_article('https://www.coramdeo.it/articoli/5-motivi-per-cui-i-bambini-fanno-parte-del-culto-principale/')
    parse_article(
        'https://proandroiddev.com/kotlin-sharedflow-or-how-i-learned-to-stop-using-rxjava-and-love-the-flow-e1b59d211715')
