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

import tweepy
from tweepy import TweepError
import secrets
from models import AuthUser, TwitterAuth

date_format = "%d/%m/%Y %H:%M:%S"

api_dict = {}


def generate_api(twitter_auth: TwitterAuth):
    auth = tweepy.OAuthHandler(secrets.twitter_consumer_api_key, secrets.twitter_consumer_secret_key)
    auth.set_access_token(twitter_auth.oauth_token, twitter_auth.oauth_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")
        return None


def get_api(user: AuthUser):
    if user.api_token in api_dict:
        return api_dict[user.api_token]
    else:
        api_dict[user.api_token] = generate_api(user)
        return api_dict[user.api_token]


def login(twitter_auth: TwitterAuth):
    api = generate_api(twitter_auth)
    me = api.me()
    return api, me.id_str, me.screen_name


def tweet(user, text):
    """
    this method write the new tweet
    :param user: who tweets
    :param text: to tweet
    :return: the status
    """
    try:
        status = get_api(user).update_status(text)
        return {'created_at': status.created_at.strftime(date_format), 'id': status.id}
    except TweepError as e:
        return {'error': str(e)}
