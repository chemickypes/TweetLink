import requests
from utils import dict_from_json
import secrets


def short_link_of(url, cuttly_api_token):
    token = cuttly_api_token if cuttly_api_token else secrets.cuttly_api_key
    s = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(token, url))
    return dict_from_json(s.text)['url']['shortLink']
