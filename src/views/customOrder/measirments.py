import datetime
import json
from flask import Response, jsonify, request
from ...database.models import Product
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError,
)

from ...utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError,
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q
class MeasurementsApi(Resource):

    def get(self):
        measured = Measurement.objects.all()
        return Response(measured.to_json(), mimetype="application/json", status=200)


    def post(self):
        try:
            measurable = request.get_json()
            measured = Measurement.objects.create(
            customer_order_id = measurable["customer_order_id"],
            shoulder = measurable["shoulder"],
            hand_length = measurable["hand_length"],
            chest_bust = measurable["chest_bust"],
            stomach = measurable["stomach"],
            top_length = measurable["top_length"],
            round_arm = measurable["round_arm"],
            waist = measurable["waist"],
            tight = measurable["tight"],
            knee = measurable["knee"],
            around_leg = measurable["around_leg"],
            leg_length = measurable["leg_length"],
            size = measurable["size"],
            other_info = measurable["other_info"]

        )

            measured.save()
            return Response(measured.to_json(), mimetype="application/json", status=201)
        except Exception as error:
            raise error



class MeasurementApi(Resource):
    def get(self,id):
        try:
            measured_spec = Measurement.objects.get(id=id)
            return Response(measured_spec.to_json(), mimetype="application/json", status=200)
        except:
            return jsonify({
                "message": "The particalar measured soecification id does not exist"
            })

    def put(self,id):
        try:
            update_measurement = Measurement.objects.get(id=id)
            measurable = request.get_json()

            update_measurement.update(
            customer_order_id = measurable["customer_order_id"],
            shoulder = measurable["shoulder"],
            hand_length = measurable["hand_length"],
            chest_bust = measurable["chest_bust"],
            stomach = measurable["stomach"],
            top_length = measurable["top_length"],
            round_arm = measurable["measurable"],
            waist = measurable["waist"],
            tight = measurable["tight"],
            knee = measurable["knee"],
            around_leg = measurable["around_leg"],
            leg_length = measurable["leg_lengh"],
            size = measurable["size"],
            other_info = measurable["other_info"]
            )

            return Response(update_measurement.to_json(), mimetype="application/json", status=200)

        except:
            return jsonify({
                "message": "an error occured"
            })

    def delete(self, id):
        try:
            measured_del = Measurement.objects.get(id=id)
            measured_del.delete()
            return jsonify({
                "message": "measured Item successfully deleted"
            })

        except:
            return jsonify({
                "message": "Something is not right"
            })


class MeasureSearchApi(Resource):
    def get(self):
        custom_order_id = request.args.get("custom_order_id")
        other_info = request.args.get("other_info")
        created_at = request.args.get("created_at")

        if custom_order_id:
            measured_search = Measurement.objects(custom_order_id__icontains = custom_order_id)
        elif other_info:
            measured_search = Measurement.objects(other_info__icontains = other_info)
        elif created_at:
            measured_search = Measurement.objects(created_at__lte = created_at)
        else:
            return jsonify({
                "message": "please enter a valid field and value"
            })

        return Response( measured_search.to_json(), mimemtype="application/json", status=200)