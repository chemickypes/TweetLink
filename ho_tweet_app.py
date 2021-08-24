"""
 Copyright (C) 2021  Angelo Moroni

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import article_parser
import hoo_tweet_link
from short_url import short_link_of
from models import TwitterAuth, AuthUser
import autheticator

from db_repo import database, DB

if not isinstance(database, DB):
    raise Exception("database must be DB (or subclass) Instance")

license_console = """TweetLink  Copyright (C) 2021  Angelo Moroni
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details."""


def tweet_url(auth_user, url):
    data = article_parser.parse_article(url)
    short_url = short_link_of(url)
    return hoo_tweet_link.tweet(auth_user, f"{data['title']}\n{' '.join(data['hashtags'])}\n{short_url}")


def analyze_url(url):
    return article_parser.parse_article(url)


def login(twitter_auth: TwitterAuth):
    api, user_id, user_nickname = hoo_tweet_link.login(twitter_auth)
    auth_user = database.get_auth_user_with_id(user_id)
    if auth_user:
        auth_user.oauth_token = twitter_auth.oauth_token
        auth_user.oauth_token_secret = twitter_auth.oauth_token_secret
        auth_user.nickname = user_nickname
    else:
        auth_user = AuthUser(
            oauth_token=twitter_auth.oauth_token,
            oauth_token_secret=twitter_auth.oauth_token,
            api_token=autheticator.generate_api_token(),
            nickname=user_nickname,
            user_id=user_id
        )
    database.store_auth_user(auth_user)
    return auth_user


if __name__ == '__main__':
    print(license_console)
    link = input('Type link to tweet:')
    s = tweet_url(link)
    if 'created_at' in s:
        print("twitted at {}".format(s['created_at']))
    else:
        print(s['error'])
