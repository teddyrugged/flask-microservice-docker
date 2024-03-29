from ..views.customOrder.customOrder import CustomOrdersApi, CustomOrderApi, CustomSearchApi
from ..views.customOrder.measirments import MeasurementsApi, MeasurementApi, MeasureSearchApi

from ..views.orderViews.ordered import OrderedsApi, OrderedApi, OrderedSearchApi
from ..views.orderViews.orderedReview import OrderedReviewsApi, OrderedReviewApi, OrderedReviewSearchApi
from ..views.orderViews.orderProduct import OrderedProductsApi, OrderedProductApi, OrderedProductSearchApi

from ..views.productViews.product import ProductsApi, ProductApi, ProductSearchApi
from ..views.productViews.productCategory import ProductCategoryApi, ProductCategoriesApi, ProductCategorySearchApi
from ..views.productViews.productSubCategory import ProductSubCategoriesApi, ProductSubCategoryApi, ProductSubCategorySearchApi

def initialize_routes(api):
    api.add_resource(CustomOrdersApi, "/api/orders")
    api.add_resource(CustomOrderApi, "/api/order/<id>")
    api.add_resource(CustomSearchApi, "/api/order/search/")


    api.add_resource(MeasurementsApi, "/api/measurement")
    api.add_resource(MeasurementApi, "/api/measurement/<id>")
    api.add_resource(MeasureSearchApi, "/api/measurement/search")





    api.add_resource(ProductsApi, "/api/products")
    api.add_resource(ProductApi, "/api/product/<id>")
    api.add_resource(ProductSearchApi, '/api/products/search/')

    api.add_resource(ProductCategoriesApi, "/api/product_category")
    api.add_resource(ProductCategoryApi, "/api/product_category/<id>")
    api.add_resource(ProductCategorySearchApi, "/api/product_category/search/")

    api.add_resource(ProductSubCategoriesApi, "/api/product_sub_category")
    api.add_resource(ProductSubCategoryApi, "/api/product_sub_category/<id>")
    api.add_resource(ProductSubCategorySearchApi, "/api/product_sub_category/search/")





    api.add_resource(OrderedsApi, "/api/ordered")
    api.add_resource(OrderedApi, "/api/ordered/<id>")
    api.add_resource(OrderedSearchApi, '/api/ordered/search/')

    api.add_resource(OrderedReviewsApi, "/api/ordered-review")
    api.add_resource(OrderedReviewApi, "/api/ordered-review/<id>")
    api.add_resource(OrderedReviewSearchApi, "/api/ordered-review/search/")

    api.add_resource(OrderedProductsApi, "/api/ordered-product")
    api.add_resource(OrderedProductApi, "/api/ordered-product/<id>")
    api.add_resource(OrderedProductSearchApi, "/api/ordered-product/search/")





