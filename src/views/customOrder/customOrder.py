from flask import Response, jsonify, request
from flask_restful import Resource
from ...database.models import CustomOrder
import datetime
import json
from ...database.models import Product

from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError,
)

from ...utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError,
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q
class CustomOrdersApi(Resource):

    def get(self):
        '''The purpose of this function is for users to get the general product'''
        orders = CustomOrder.objects.all()
        return Response( orders.to_json(), mimetype="application/json", status=200)

    def post(self):
        '''The purpose of this function is to be able to make a general post for all orders available'''
        try:
            order_data = request.get_json()
            order = CustomOrder.objects.create(
                product_category_id = order_data["product_category_id"],
                product_sub_category_id = order_data["product_sub_category_id"],
                gender = order_data["gender"],
                size = order_data["size"]
            )
            order.save()
            return Response(order.to_json(), mimetype="application/json", status=201)
        except Exception as error:
            raise error


# creating the custom package for the specific get method with the update and delete
class CustomOrderApi(Resource):
    def get(self, id):
        '''This function will help track a specific order'''
        try:
            order = CustomOrder.objects.get(id=id).to_json()
            return Response(order, mimetype="application/json", status=200)
        except:
            return jsonify(
                message = "the Id your enter does not exiting",
                status = 400
            )


    def put(self, id):
        try:
            order_update = CustomOrder.objects.get(id=id)
            order_data = request.get_json()

            order_update.update(
                product_category_id = order_data["product_category_id"],
                product_sub_category_id = order_data["product_sub_category"],
                gender = order_data["gender"],
                size = order_data["size"]
            )
            order_update.save()
            return Response(order_update.to_json(), mimetype="application/json", status=201)
        except Exception as error:
            raise error


    def delete(self, id):
        try:
            cancel_order = CustomOrder.objects.get(id=id)
            cancel_order.delete()
            return jsonify({
                "message": "You have successfully cancelled the order"
            })
        except Exception as error:
            raise error

#Creating the Custom search order
class CustomSearchApi(Resource):
    def get(self):
        product_category_id = request.args.get("product_category_id")
        product_sub_category_id = request.args.get("product_sub_category_id")
        gender = request.args.get("gender")
        size = request.args.get("size")
        created_at = request.args.get("created_at")

        if product_category_id:
            orders = CustomOrder.objects(product_category_id__icontains = product_category_id)
        elif product_sub_category_id:
            orders = CustomOrder.objects(product_sub_category_id__icontains = product_sub_category_id)
        elif gender:
            orders = CustomOrder.objects(gender__icontains = gender)
        elif size:
            orders = CustomOrder.objects(size__icontains = size)
        elif created_at:
            orders = CustomOrder.objects(created_at__lte = created_at)
        else:
            return jsonify({
                "message": "Kindly enter a valid field and value"
            })

        return Response(orders.to_json(), mimetype="application/json", status=200)