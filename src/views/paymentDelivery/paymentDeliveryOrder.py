import datetime
import json
from flask import Response, jsonify, request
from ...database.models import PaymentDeliveryOrder
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError,
)

from ...utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError,
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q