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
import uvicorn

from models import TwitterAuth, Auth, LinkBundle
import ho_tweet_app as tweet_link_app
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


@app.post('/analyze_url')
async def analyze_url(tweet_bundle: LinkBundle):
    return tweet_link_app.analyze_url(tweet_bundle.link)


@app.post('/tweet')
async def tweet(tweet_bundle: LinkBundle, api_token: Optional[str] = None):
    user = autheticator.check_api_token(api_token)
    if user:
        return tweet_link_app.tweet_url(user, tweet_bundle.link)
    else:
        raise HTTPException(401, 'api_token not valid')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
