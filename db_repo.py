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
from models import AuthUser, TwitterAuth

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Example
db = {'gen11': AuthUser(
    oauth_token='13360----pfSh3F',
    oauth_token_secret='n3Ib5IwKnuf5v------LfwYCQErOt6jQB',
    api_token='---',
    nickname='@hoo---mic'
)}


class DB:
    def get_auth_user(self, api_token):
        return db[api_token]

    def get_auth_user_with(self, nickname):
        return None

    def store_auth_user(self, user: AuthUser):
        pass


class FirebaseDB(DB):
    def __init__(self):
        cred = credentials.Certificate("hootweetlink_firebase.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_auth_user(self, api_token):
        doc = self.db.collection(u'authentication').document(api_token).get().to_dict()
        return AuthUser(**doc)

    def get_auth_user_with(self, nickname):
        docs = self.db.collection(u'authentication').where(u'nickname', u'==', nickname).stream()
        user = None
        for doc in docs:
            user = AuthUser(**doc.to_dict())
        return user

    def store_auth_user(self, user: AuthUser):
        self.db.collection(u'authentication').document(user.api_token).set(user.dict())


database = FirebaseDB()
