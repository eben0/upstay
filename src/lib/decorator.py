import logging
from functools import wraps
from typing import Tuple, Callable, Any, Dict

from flask import jsonify, request, Response

logger = logging.getLogger()


def json_response(f) -> Callable[[Any, Any], Tuple[Response, int]]:
    """
    decorator function that wraps the json response
    and handles the error message
    :param f: route function
    :return: response
    """

    @wraps(f)
    def decorated_function(*args, **kwargs) -> Tuple[Response, int]:
        try:
            resp = f(*args, **kwargs)
            logger.debug(f"{request.path} response: {str(resp)[:100]}")
            return jsonify(error=None, status=200, results=resp), 200
        except Exception as e:
            logger.error(f"{request.path} error", e)
            return jsonify(error=str(e), status=500, results=[]), 500

    return decorated_function
