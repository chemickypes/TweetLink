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
from models import AuthUser

db = {'gen11': AuthUser(
    oauth_token='1336035132587839488-lSs7GSZFC1vswdtYwGEPCiU8pfSh3F',
    oauth_token_secret='n3Ib5IwKnuf5vdnEYT5gqGWY4VVnqy6LfwYCQErOt6jQB',
    api_token='gen11',
    nickname='@hooloovoochimic'
)}


class DB:
    def get_auth_user(self, api_token):
        return db[api_token]


database = DB()
