import requests
from utils import dict_from_json
import secrets


def short_link_of(url):
    s = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(secrets.cuttly_api_key, url))
    return dict_from_json(s.text)['url']['shortLink']