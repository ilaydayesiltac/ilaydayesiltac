import json
import uuid

from application.core.app_models import BaseResponse
from application.core.db_models import Link
from application import db
from flask import abort, request, jsonify
from user_agents import parse
from application.utils.tools import Tools


class LinkUtils:
    @staticmethod
    def generate_short_url(original_url):
        response = BaseResponse()
        key = Tools.generate_random_key(3)
        link = Link(key = key, original_url=original_url, counter=0, extra_information=[], private_key=str(uuid.uuid4()))

        if Tools.is_valid_url(original_url):
            db.session.add(link)
            db.session.commit()
        else:
            response.fail(500, message='is not valid url.')

        response.data = {'key': key, 'private_key': link.private_key}
        return response

    @staticmethod
    def redirect_to_original_url(key):
        response = BaseResponse()
        print(request.headers.get('Referer'))
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
            ip_address_list = []
            browser_list = []
            operating_system_list = []
            origin_list = []

            for statistic in statistic_data:
                ip_address_list.append(statistic['ip_address'])
                browser_list.append(statistic['browser'])
                operating_system_list.append(statistic['operating_system'])
                origin_list.append(statistic['origin'])

            browser_count = {}
            origin_count = {}
            operating_system_count = {}

            for browser in browser_list:
                if browser in browser_count:
                    browser_count[browser] += 1
                else:
                    browser_count[browser] = 1

            for operating_system in operating_system_list:
                if operating_system in operating_system_count:
                    operating_system_count[operating_system] += 1
                else:
                    operating_system_count[operating_system] = 1

            for origin in origin_list:
                if origin in origin_count:
                    origin_count[origin] += 1
                else:
                    origin_count[origin] = 1

            response.data['browsers'] = browser_count
            response.data['operating_systems'] = operating_system_count
            response.data['origins'] = origin_count
            response.data['unique_ip_addresses'] = list(set(ip_address_list))
        return response


def get_user_agent():
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)

    browser = user_agent.browser.family
    operating_system = user_agent.os.family
    client_ip = request.remote_addr
    origin = request.headers.get('Origin')

    extra_information = {
        "ip_address": client_ip,
        "browser": browser,
        "operating_system": operating_system,
        "origin": origin,
    }

    return extra_information
