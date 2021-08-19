import tweepy
from tweepy import TweepError
import secrets

auth = tweepy.OAuthHandler(secrets.twitter_consumer_api_key, secrets.twitter_consumer_secret_key)
auth.set_access_token(secrets.twitter_access_token, secrets.twitter_secret_token)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

date_format = "%d/%m/%Y %H:%M:%S"


def tweet(text):
    """
    this method write the new tweet
    :param text: to tweet
    :return: the status
    """
    try:
        status = api.update_status(text)
        return {'created_at': status.created_at.strftime(date_format), 'id': status.id}
    except TweepError as e:
        return {'error': str(e)}
