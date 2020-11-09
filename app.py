from roles import USER_ROLES
from typing import List

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/form-cmd<string:event_id>/<string:user_csv>')
class MoreBars(Resource):
    def post(self, event_id: str, user_csv: str):
        print(f"event_id = {event_id}")
        print(f"user_csv = {user_csv}")
        return create_raid_helper_cmd(event_id=event_id, user_csv=user_csv)


def get_role_for_user(user: str) -> str:
    matches = [role for role, users_in_role in USER_ROLES.items()
               if user.lower() in [usr.lower() for usr in users_in_role]]
    return "" if not matches else matches[0]


def get_role_cmd_for_role_and_users(users: List[str], role: str) -> str:
    all_in_role = USER_ROLES[role]
    matching_for_role = [user for user in all_in_role if user.lower() in [usr.lower() for usr in users]]
    user_list = ', '.join(sorted(matching_for_role))
    return f"{role} [{user_list}]"


def get_roles_for_users(user_csv: str) -> List[str]:
    users = user_csv.split(",")
    user_roles = [get_role_for_user(user) for user in users]
    unique_user_roles = list(set(user_roles))
    role_cmds = [get_role_cmd_for_role_and_users(users=users, role=role) for role in unique_user_roles]
    return role_cmds


def create_raid_helper_cmd(event_id: str, user_csv: str) -> str:
    return f"!adduser {event_id} {' '.join(get_roles_for_users(user_csv))}"


if __name__ == '__main__':
    app.run(debug=True)
