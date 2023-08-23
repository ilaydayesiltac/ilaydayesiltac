import json
import uuid

from application.core.app_models import BaseResponse
from application.core.db_models import Link
from application import db
from flask import abort, request
from user_agents import parse
from application.utils.tools import Tools


class LinkUtils:
    @staticmethod
    def generate_short_url(original_url):
        response = BaseResponse()
        key = Tools.generate_random_key(3)
        link = Link(key=key, original_url=original_url, counter=0, extra_information=[], private_key=str(uuid.uuid4()))

        if Tools.is_valid_url(original_url):
            db.session.add(link)
            db.session.commit()
        else:
            response.fail(500, message='is not valid url.')
        # https: // smart_url.at / bhtR5
        response.data = {'key': key, 'private_key': link.private_key}
        return response

    @staticmethod
    def redirect_to_original_url(key):
        response = BaseResponse()
        # check whether the key is available in database or not
        link = Link.query.filter_by(key=key).first()
        if link is None:
            response.fail(400, 'the key is not defined!')
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
    def get_stats(key, private_key):
        response = BaseResponse()
        link = Link.query.filter(Link.key == key,
                                 Link.private_key == private_key).first()  # get row according to url without duplicates

        if link is None:
            abort(400, "key or private key could not be found!")

        # Assuming link.extra_information is a list # Assuming you're receiving the JSON as bytes
        response.data = {
            "url": link.original_url,
            "counter": link.counter
        }
        if len(link.extra_information) != 0:
            statistic_data = json.loads(link.extra_information)
            ip_addresses = []
            browsers = []
            operating_systems = []

            for statistic in statistic_data:
                print(statistic['ip_address'])
                ip_addresses.append(statistic['ip_address'])
                browsers.append(statistic['browser'])
                operating_systems.append(statistic['operating_system'])

            response.data["ip_addresses"] = list(set(ip_addresses))
            response.data["browsers"] = list(set(browsers))
            response.data["operating_systems"] = list(set(operating_systems))

        return response

    @staticmethod
    def get_url_stat_by_owner(key):
        response = BaseResponse()
        print(key)
        return response


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
