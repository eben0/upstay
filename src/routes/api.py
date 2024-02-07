import logging

from flask import Blueprint, request

from dao.reservation_dao import ReservationDao
from lib.decorator import json_response

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")

logger = logging.getLogger(__name__)
reservation_dao = ReservationDao()


# /api/reservation/<id>
@api_bp.route("/reservation/<id>")
@json_response
def get_reservation(id):
    return reservation_dao.get_reservation(id).to_dict()


# /api/availability/<id>
@api_bp.route("/availability/<id>")
@json_response
def get_availability(id):
    return reservation_dao.get_availability(id)
