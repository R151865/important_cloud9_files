from essentials_kit_management.interactors.presenters. \
    order_presenter_interface import OrderPresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import \
    INVALID_ORDER_ID


class OrderPresenterImplementation(OrderPresenterInterface):

    def raise_invalid_order_id_exception(self):
        raise NotFound(*INVALID_ORDER_ID)
