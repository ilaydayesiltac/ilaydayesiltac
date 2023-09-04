from flask import request, jsonify, abort

from application.core.app_models import BaseResponse
from application.core.utils.link_utils import LinkUtils
from application.userland.controller import mod_userland
from flask import redirect


@mod_userland.route('/original_url', methods=['GET'])
def generate_short_url():
    original_url = request.args.get('original_url')
    response = LinkUtils.generate_short_url(original_url)
    return jsonify(response.__dict__)


@mod_userland.route('/<key>', methods=['GET'])
def redirect_to_original_url(key):
    response = LinkUtils.redirect_to_original_url(key)

    if response.data is None:
        return jsonify(response.__dict__)

    return jsonify(response.__dict__)


@mod_userland.route('/stats/<key>', methods=['GET'])
def get_stats(key):
    private_key = request.args.get('private_key')
    response = LinkUtils.get_stats(key, private_key)
    return jsonify(response.__dict__)
