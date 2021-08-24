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
from models import TwitterAuth, Auth, TweetBundle
import app as tweet_link_app
from typing import Optional
from fastapi import FastAPI, HTTPException
import autheticator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login")
async def login(twitter_auth: TwitterAuth):
    return Auth("")


@app.post('/tweet')
async def tweet(tweet_bundle: TweetBundle, api_token: Optional[str] = None):
    user = autheticator.check_api_token(api_token)
    if user:
        return tweet_link_app.tweet_link(tweet_bundle.link)
    else:
        raise HTTPException(401, 'api_token not valid')
