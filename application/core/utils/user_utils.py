from werkzeug.security import generate_password_hash, check_password_hash

from application.core.app_models import BaseResponse
from application.core.db_models import Users
from application import db
from flask import abort


class UserUtils:
    @staticmethod
    def sign_up_user(email, password):
        response = BaseResponse()
        already_have_user = Users.query.filter(Users.email == email).first()
        if not already_have_user:
            if email and password:
                hashed_password = generate_password_hash(password, method='sha256')
                user = Users(
                    email=email,
                    password=hashed_password
                )
                db.session.add(user)
                db.session.commit()
        else:
            response = response.fail()
        return response

    @staticmethod
    def sign_in_user(email, password):
        response = BaseResponse()
        user = Users.query.filter(Users.email == email).first()
        if user:
            check_password = check_password_hash(user.password, password)
            if check_password:
                return response
        else:
            response = response.fail(message='User Not Found!')
        return response
