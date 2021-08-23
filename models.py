from pydantic import BaseModel


class TwitterAuth(BaseModel):
    oauth_token: str
    oauth_token_secret: str


class Auth(BaseModel):
    api_token: str


class TweetBundle(BaseModel):
    link: str
