import json
import random
import string

import requests

from application.core.app_models import BaseResponse
from application.core.db_models import Link
from application import db
from flask import abort, redirect, request
from user_agents import parse
from application.utils.tools import Tools


class LinkUtils:
    @staticmethod
    def generate_short_url(original_url):
        response = BaseResponse()
        key = Tools.generate_random_key(3)
        if Tools.is_valid_url(original_url):
            link = Link(key=key, original_url=original_url, counter=0, extra_information=[])
            db.session.add(link)
            db.session.commit()
        else:
            response.fail(500, message='is not valid url.')
        response.data = key
        return response

    @staticmethod
    def redirect_to_original_url(key):
        response = BaseResponse()
        # check whether the key is available in database or not
        link = Link.query.filter_by(key=key).first()
        if link is None:
            response.fail(500, 'the key is not defined!')
            return response

        link.counter += 1

        existing_extra_information_array = []
        if len(link.extra_information) != 0:
            existing_extra_information_array = json.loads(link.extra_information)
        user_agent_information = get_user_agent()
        existing_extra_information_array.append(user_agent_information)

        updated_data = json.dumps(existing_extra_information_array)

        link.extra_information = updated_data
        db.session.commit()
        response.data = link.original_url

        return response

    @staticmethod
    def get_stats():
        response = BaseResponse()
        links = Link.query.distinct('original_url').all()  # get row according to url without duplicates
        data = []
        for link in links:
            counter = 0
            all_same_url = Link.query.filter_by(original_url=link.original_url).all()

            # calculate total counter number by url
            for i in all_same_url:
                counter += i.counter

            concatenated_extra_information = []
            for inner_array in all_same_url:
                if len(inner_array.extra_information) == 0:
                    continue
                extra_info = json.loads(inner_array.extra_information)
                for obj in extra_info:
                    concatenated_extra_information.append(obj)

            data.append({
                "url": all_same_url[0].original_url,
                "counter": counter,
                "extra_information": concatenated_extra_information
            })
        response.data = data
        return response


"""       
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
"""


def get_user_agent():
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)

    browser = user_agent.browser.family
    operating_system = user_agent.os.family
    client_ip = request.remote_addr

    extra_information = {
        "ip_address": client_ip,
        "browser": browser,
        "operating_system": operating_system,
    }

    return extra_information
