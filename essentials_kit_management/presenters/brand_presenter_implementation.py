from essentials_kit_management.interactors.presenters. \
    brand_presenter_interface import BrandPresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import \
    INVALID_BRAND_ID


class BrandPresenterImplementation(BrandPresenterInterface):

    def raise_invalid_brand_id_exception(self):
        raise NotFound(*INVALID_BRAND_ID)
