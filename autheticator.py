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

from db_repo import database, DB
import random
import string

if not isinstance(database, DB):
    raise Exception("database must be DB (or subclass) Instance")


def check_api_token(api_token):
    auth_user = database.get_auth_user(api_token)
    if api_token:
        return auth_user
    else:
        return None


def generate_api_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
