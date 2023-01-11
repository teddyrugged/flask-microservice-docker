from datetime import datetime
from .db import db


class OrderProduct(db.Document):
    product_id = db.IntField(required=True)
    status = db.StringField()
    added_price = db.IntField()
    quantity = db.IntField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class Ordered(db.Document):
    ordered_product_id = db.IntField(required=True)
    ordered_date = db.DateTimeField(auto_now_add=True, default=datetime.now)
    ordered = db.BooleanField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class OrderedReview(db.Document):
    ordered_id = db.IntField(required=True)
    rating = db.IntField()
    review = db.StringField()
    return_request = db.BooleanField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }
