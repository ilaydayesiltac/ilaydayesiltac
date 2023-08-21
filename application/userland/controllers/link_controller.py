from flask import request, jsonify, abort

from application.core.app_models import BaseResponse
from application.core.utils.link_utils import LinkUtils
from application.userland.controller import mod_userland
from flask import redirect


@mod_userland.route('/short_url', methods=['GET'])
def short_url():
    original_url = request.args.get('original_url')
    response = LinkUtils.generate_short_url(original_url)
    return jsonify(response.__dict__)


# 641560
@mod_userland.route('/<key>', methods=['GET'])
def redirect_to_original_url(key):
    response = LinkUtils.redirect_to_original_url(key)

    if response.data is None:
        return jsonify(response.__dict__)

    return redirect(response.data)


@mod_userland.route('/owner_key', methods=['GET'])
def show_original_url_stat():
    key = request.args.get('key')

    response = LinkUtils.get_url_stat_by_owner(key)
    return jsonify(response.__dict__)


@mod_userland.route('/stats', methods=['GET'])
def get_stats():
    response = LinkUtils.get_stats()
    return redirect(response)
