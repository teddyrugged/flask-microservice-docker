
import datetime
import json
from flask import Response, jsonify, request
from ..database.models import Ordered
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError,
)

from ..utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError,
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q

class OrderedsApi(Resource):

    def get(self):
        ordereds = Ordered.objects.all()
        return Response( ordereds.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            ordered = Ordered.objects.create(
                ordered_product_id  = data["ordered_product_id"],
                ordered_date = data["ordered_date"],
                ordered = data["ordered"],
            )
            ordered.save()
            return Response(ordered.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class OrderedApi(Resource):
    def get(self, id):
        try:
            ordered = Ordered.objects.get(id=id).to_json()
            return Response(ordered, mimetype="application/json", status=200 )
        except:
            return jsonify(

                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:
            update_ordered = Ordered.objects.get(id=id)
            data = request.get_json()

            update_ordered.update(
                ordered_product_id  = data["ordered_product_id"],
                ordered_date = data["ordered_date"],
                ordered = data["ordered"],
            )
            update_ordered.save()
            return Response(update_ordered.to_json(), mimetype="application/json", status=200)
        except Exception:
            raise  InternalServerError


    def delete(self, id):
        try:
            delete_ordered = Ordered.objects.get(id=id)
            delete_ordered.delete()
            return jsonify({
                "message": "ordered deleted successfully"
            })
        except Exception:
            raise InternalServerError


class OrderedSearchApi(Resource):
     def get(self):
        ordered_product_id  = request.args.get("ordered_product_id")
        ordered_date = request.args.get("ordered_date")
        ordered = request.args.get("ordered")
        created_at = request.args.get("created_at")

        if ordered_product_id:
            ordereds = Ordered.objects(ordered_product__icontains = ordered_product_id)
        elif ordered_date:
            ordereds = Ordered.objects(ordered_date__lte = ordered_date)
        elif ordered :
            ordereds = Ordered.objects(ordered__lte = ordered)
        elif created_at:
            ordereds =  Ordered.objects(created_at__lte = datetime.datetime.now())
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })


        return Response( ordereds.to_json(), mimetype="application/json", status=200 )






# from flask import request
# from flask_restful import Resource

# class Ordered(Resource):
#   def get(self, id):
#     # Retrieve the ordered with the given id
#     ordered = OrderedModel.find_by_id(id)
#     if ordered:
#       return ordered.json()
#     return {'message': 'Ordered not found'}, 404

#   def post(self, id):
#     # Check if the ordered already exists
#     if OrderedModel.find_by_id(id):
#       return {'message': "An ordered with id '{}' already exists".format(id)}, 400

#     # Create a new ordered
#     data = request.get_json()
#     ordered = OrderedModel(id, **data)
#     try:
#       ordered.save_to_db()
#     except:
#       return {'message': 'An error occurred while creating the ordered'}, 500

#     return ordered.json(), 201

#   def delete(self, id):
#     # Delete the ordered with the given id
#     ordered = OrderedModel.find_by_id(id)
#     if ordered:
#       ordered.delete_from_db()
#       return {'message': 'Ordered deleted'}
#     return {'message': 'Ordered not found'}, 404

#   def put(self, id):
#     # Update the ordered with the given id
#     data = request.get_json()
#     ordered = OrderedModel.find_by_id(id)
#     if ordered:
#       ordered.name = data['name']
#       ordered.save_to_db()
#       return {'message': 'Ordered updated'}
#     return {'message': 'Ordered not found'}, 404
