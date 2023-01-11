
import datetime
import json
from flask import Response, jsonify, request
from ..database.models import OrderedReview
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError,
)

from ..utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError,
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q

class OrderedReviewsApi(Resource):

    def get(self):
        orderedreviews = OrderedReview.objects.all()
        return Response( orderedreviews.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            orderedreview = OrderedReview.objects.create(
                ordered_id  = data["ordered_id"],
                rating = data["rating"],
                review = data["review"],
                return_request = data["return_request"],
            )
            orderedreview.save()
            return Response(orderedreview.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class OrderedReviewApi(Resource):
    def get(self, id):
        try:
            orderedreview = OrderedReview.objects.get(id=id).to_json()
            return Response(orderedreview, mimetype="application/json", status=200 )
        except:
            return jsonify(

                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:
            update_orderedreview = OrderedReview.objects.get(id=id)
            data = request.get_json()

            update_ordered.update(
                ordered_product_id  = data["ordered_product_id"],
                ordered_date = data["ordered_date"],
                ordered = data["ordered"],
            )
            update_orderedreview.save()
            return Response(update_orderedreview.to_json(), mimetype="application/json", status=200)
        except Exception:
            raise  InternalServerError


    def delete(self, id):
        try:
            delete_orderedreview = OrderedReview.objects.get(id=id)
            delete_orderedreview.delete()
            return jsonify({
                "message": "ordered deleted successfully"
            })
        except Exception:
            raise InternalServerError


class OrderedReviewSearchApi(Resource):
     def get(self):
        ordered_product_id  = request.args.get("ordered_product_id")
        ordered_date = request.args.get("ordered_date")
        ordered = request.args.get("ordered")
        created_at = request.args.get("created_at")

        if ordered_product_id:
            ordereds = Ordered.objects(ordered_date_id__icontains = ordered_product_id)
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

# class OrderedReview(Resource):
#   def get(self, id):
#     # Retrieve the ordered review with the given id
#     ordered_review = OrderedReviewModel.find_by_id(id)
#     if ordered_review:
#       return ordered_review.json()
#     return {'message': 'Ordered review not found'}, 404

#   def post(self, id):
#     # Check if the ordered review already exists
#     if OrderedReviewModel.find_by_id(id):
#       return {'message': "An ordered review with id '{}' already exists".format(id)}, 400

#     # Create a new ordered review
#     data = request.get_json()
#     ordered_review = OrderedReviewModel(id, **data)
#     try:
#       ordered_review.save_to_db()
#     except:
#       return {'message': 'An error occurred while creating the ordered review'}, 500

#     return ordered_review.json(), 201

#   def delete(self, id):
#     # Delete the ordered review with the given id
#     ordered_review = OrderedReviewModel.find_by_id(id)
#     if ordered_review:
#       ordered_review.delete_from_db()
#       return {'message': 'Ordered review deleted'}
#     return {'message': 'Ordered review not found'}, 404

#   def put(self, id):
#     # Update the ordered review with the given id
#     data = request.get_json()
#     ordered_review = OrderedReviewModel.find_by_id(id)
#     if ordered_review:
#       ordered_review.name = data['name']
#       ordered_review.save_to_db()
#       return {'message': 'Ordered review updated'}
#     return {'message': 'Ordered review not found'}, 404
