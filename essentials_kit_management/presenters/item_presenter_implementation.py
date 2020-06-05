from essentials_kit_management.interactors.presenters. \
    item_presenter_interface import ItemPresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import \
    INVALID_ITEM_ID


class ItemPresenterImplementation(ItemPresenterInterface):

    def raise_invalid_item_id_exception(self):
        raise NotFound(*INVALID_ITEM_ID)
