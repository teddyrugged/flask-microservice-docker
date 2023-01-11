from ..views.ordered import OrderedsApi, OrderedApi, OrderedSearchApi
from ..views.orderedReview import OrderedReviewsApi, OrderedReviewApi, OrderedReviewSearchApi
from ..views.orderProduct import OrderedProductsApi, OrderedProductApi, OrderedProductSearchApi


def initialize_routes(api):
    api.add_resource(OrderedsApi, "/api/ordered")
    api.add_resource(OrderedApi, "/api/ordered/<id>")
    api.add_resource(OrderedSearchApi, '/api/ordered/search/')

    api.add_resource(OrderedReviewsApi, "/api/ordered-review")
    api.add_resource(OrderedReviewApi, "/api/ordered-review/<id>")
    api.add_resource(OrderedReviewSearchApi, "/api/ordered-review/search/")

    api.add_resource(OrderedProductsApi, "/api/ordered-product")
    api.add_resource(OrderedProductApi, "/api/ordered-product/<id>")
    api.add_resource(OrderedProductSearchApi, "/api/ordered-product/search/")





