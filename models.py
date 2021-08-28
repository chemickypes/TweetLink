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
from pydantic import BaseModel


class TwitterAuth(BaseModel):
    oauth_token: str
    oauth_token_secret: str


class AuthUser(TwitterAuth):
    api_token: str
    nickname: str
    user_id: str
    cuttly_token: str


class Auth(BaseModel):
    api_token: str


class LinkBundle(BaseModel):
    link: str


class ApiKeyBundle(BaseModel):
    api_key: str
