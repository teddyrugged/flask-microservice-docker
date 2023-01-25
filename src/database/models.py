from datetime import datetime
from .db import db


class Product(db.Document):
    product_name = db.StringField(required=True)
    sale_price = db.IntField()
    discount_price = db.IntField()
    total_cost_price = db.IntField()
    color = db.StringField()
    image = db.StringField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class ProductCategory(db.Document):
    category_name = db.StringField(required=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class ProductSubCategory(db.Document):
    fabric_type = db.StringField(required=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }






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
