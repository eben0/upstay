from datetime import datetime

import pandas as pd


class Reservation:
    def __init__(
        self, _id, room_id, hotel_id, guest_name, arrival_date, nights, room_count
    ):
        self.id = _id
        self.room_id = room_id
        self.hotel_id = hotel_id
        self.guest_name = guest_name
        self.arrival_date: datetime = pd.to_datetime(arrival_date)
        self.nights = nights
        self.room_count = room_count

    @staticmethod
    def from_dataframe(df):
        return Reservation(
            df["reservation_id"],
            df["room_id"],
            df["hotel_id"],
            df["guest_name"],
            df["arrival_date"],
            df["nights"],
            df["room_count"],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "hotel_id": self.hotel_id,
            "guest_name": self.guest_name,
            "arrival_date": self.arrival_date,
            "nights": self.nights,
            "room_count": self.room_count,
        }
