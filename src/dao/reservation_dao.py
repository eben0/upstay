import logging
from typing import List, Dict
from datetime import timedelta, datetime, timezone

import pandas as pd

from lib.config import Config
from models.reservation import Reservation

logger = logging.getLogger()


class ReservationDao:
    def __init__(self):
        self.config = Config.instance().all()

    def read_csv(self):
        return pd.read_csv(self.config["reservation"]["reservations_path"])

    def read_inventory(self):
        return pd.read_json(self.config["reservation"]["inventory_path"])

    def get_reservation(self, id) -> Reservation:
        df = self.read_csv()
        df = df[df["reservation_id"] == id]
        for _, row in df.iterrows():
            return Reservation.from_dataframe(row)

    def get_availability(self, id) -> Dict:

        room_reservation = self.get_reservation(id)
        room_leave = room_reservation.arrival_date + timedelta(days=room_reservation.nights)

        inventory = self.read_inventory().to_dict()["inventory"]
        df = self.read_csv()
        df = df[df["reservation_id"] != id]

        for _, row in df.iterrows():
            reservation = Reservation.from_dataframe(row)
            leave = reservation.arrival_date + timedelta(days=reservation.nights)

            if reservation.arrival_date >= room_reservation.arrival_date and leave <= room_leave:
                inventory[reservation.room_id] -= 1

        return inventory
