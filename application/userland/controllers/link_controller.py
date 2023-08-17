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
@mod_userland.route('/redirect_to_original_url', methods=['GET'])
def redirect_to_original_url():
    short_url = request.args.get('key')

    response = LinkUtils.redirect_to_original_url(short_url)
    return jsonify({"url": response})


@mod_userland.route('/stats', methods=['GET'])
def get_stats():
    response = LinkUtils.get_stats()
    return redirect(response)
