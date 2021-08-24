from db_repo import database, DB

if not isinstance(database, DB):
    raise Exception("database must be DB (or subclass) Instance")


def check_api_token(api_token):
    auth_user = database.get_auth_user(api_token)
    if api_token:
        return auth_user
    else:
        return None
