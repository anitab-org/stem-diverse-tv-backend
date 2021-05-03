from app.database.models.users import UserModel
import requests
import json
from typing import Dict
from firebase_admin import auth
from os import environ
from app.utils.email_utils import send_email_verification_message


class UserDAO:
    """Data access object for user"""

    @staticmethod
    def create_user(data: Dict[str, str]):
        name = data["name"]
        username = data["username"]
        email = data["email"]
        password = data["password"]
        terms_and_conditions_checked = data["terms_and_conditions_checked"]

        existing_user = UserModel.find_by_username(username)
        if existing_user:
            return {"message": "Acount already exists with this username"}, 400
        try:
            user = auth.create_user(
                email=email,
                email_verified=False,
                password=password,
                display_name=name,
                disabled=False,
            )

            link = auth.generate_email_verification_link(
                email, action_code_settings=None
            )

            send_email_verification_message(link, email)

        except Exception as e:
            return {"message": str(e)}, 400

        try:
            firebase_details = auth.get_user_by_email(email)
            uid = firebase_details.uid
            firebase_email = firebase_details.email
            user = UserModel(
                name, uid, username, email, password, terms_and_conditions_checked
            )
            user.save_to_db()
        except Exception as e:
            return {"message": str(e)}, 400

        return {
            "message": "User was created successfully. Please check your email to verify the account",
        }, 201

    @staticmethod
    def authenticate(email: str, password: str):
        """ User login process"""

        try:
            user = auth.get_user_by_email(email)
            if not user.email_verified:
                return {
                    "message": "Email is not verified, Please verify email first"
                }, 400

        except Exception as e:
            return {"message": e.args[0]}, 400

        json_string = {"email": email, "password": password, "returnSecureToken": True}
        API_KEY = environ.get("API_KEY")
        url = (
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key="
            + API_KEY
        )
        res = requests.post(url, data=json_string)
        json_response = json.loads(res.text)

        if "error" in json_response.keys():
            error_message = json_response["error"]
            if error_message["message"] == "INVALID_PASSWORD":
                return {"message": "Password is incorrect"}, 401
            else:
                return {"message": error_message["message"]}, 401

        return json_response, 200
