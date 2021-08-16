import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.twitter_consumer_api_key, secrets.twitter_consumer_secret_key)
auth.set_access_token(secrets.twitter_access_token, secrets.twitter_secret_token)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def tweet(text):
    """
    this method write the new tweet
    :param text: to tweet
    :return: the status
    """
    status = api.update_status(text)
    return status
