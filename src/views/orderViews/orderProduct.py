from flask import Response, jsonify, request,Flask
from flask_restful import Resource,Api
from ..database.models import OrderProduct
import datetime
from mongoengine.errors import (
    FieldDoesNotExist, DoesNotExist,ValidationError, InvalidQueryError
)
from ..utility.errors import (
    SchemaValidationError, InternalServerError, UpdatingProductCategoryError,
    DeletingProductCategoryError, ProductCategoryNotExistsError,FieldDoesNotExistError
)



class OrderedProductsApi(Resource):

    def get(self):
        ordered_prod = OrderedProduct.objects.all()
        return Response(  ordered_prod.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            ordered_prod = OrderedProduct.objects.create(
                product_id  = data["product_id"],
                status = data["status"],
                added_price = data["added_price"],
                quantity = data["quantity"],
            )
            ordered.save()
            return Response(ordered.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class OrderedProductApi(Resource):
    def get(self, id):
        try:
            ordered_prod = OrderedProduct.objects.get(id=id).to_json()
            return Response(ordered_prod, mimetype="application/json", status=200 )
        except:
            return jsonify(

                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:
            update_ordered_prod = OrderedProduct.objects.get(id=id)
            data = request.get_json()

            update_oordered_prod.update(
                product_id  = data["product_id"],
                status = data["status"],
                added_price = data["added_price"],
                quantity = data["quantity"],
            )
            update_ordered_prod.save()
            return Response(update_ordered_prod.to_json(), mimetype="application/json", status=200)
        except Exception:
            raise  InternalServerError


    def delete(self, id):
        try:
            ordered_prod = OrderedProduct.objects.get(id=id)
            ordered_prod.delete()
            return jsonify({
                "message": "orderedproduct deleted successfully"
            })
        except Exception:
            raise InternalServerError


class OrderedProductSearchApi(Resource):
     def get(self):
        product_id  = request.args.get("product_id")
        status = request.args.get("status")
        added_price = request.args.get("added_price")
        quantity = request.args.get("quantity")
        created_at = request.args.get("created_at")

        if product_id:
            ordered_prod = OrderedProduct.objects(product_id__icontains = product_id)
        elif status:
            ordered_prod = OrderedProduct.objects(status__lte = staus)
        elif added_price :
            ordered_prod = OrderedProduct.objects(added_price__lte = added_price)
        elif quantity:
            ordered_prod = OrderedProduct.objects(quantity__lte = quantity)
        elif created_at:
            ordered_prod =  OrderedProduct.objects(created_at__lte = datetime.datetime.now())

        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })


        return Response( ordered_prod.to_json(), mimetype="application/json", status=200 )









# class OrderProductApi(Resource):

#     def get(self):
#         # order_product = OrderProduct.objects.all()
#      response = {"status": 400, "message": "Product not ordered"}

#      def post(self):
#          user_data = request.get_json()
#          first_name = user_data["first_name"]
#          last_name = user_data["last_name"]
#          email = user_data["email"]
#          user = User(first_name=first_name, last_name=last_name, email=email)
#          db.session.add(user)
#          db.session.commit()
#          self.response["status"] = 201
#          self.response["message"] = "Product  order successfully"
#          return self.response, 201



# class OrderProductApi(Resource):
#     def get(self, order_id):
#         # retrieve the specified order from the database
#         order = Order.query.get(order_id)
#         if not order:
#             return {'error': 'Order not found'}, 404
#         # return the order data as a JSON response
#         return {'id': order.id, 'customer_name': order.customer_name, 'customer_address': order.customer_address, 'products': [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in order.products]}

#     def post(self):
#         # parse the request data as JSON
#         data = request.get_json()
#         # create a new Order object with the received data
#         order = Order(customer_name=data['customer_name'], customer_address=data['customer_address'])
#         # add the specified products to the order
#         for product_id in data['product_ids']:
#             product = Product.query.get(product_id)
#             if product:
#                 order.products.append(product)
#         # add the order to the database and return the order data as a JSON response
#         db.session.add(order)
#         db.session.commit()
#         return {'id': order.id, 'customer_name': order.customer_name, 'customer_address': order.customer_address, 'products': [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in order.products]}

