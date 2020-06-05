from essentials_kit_management.interactors.presenters. \
    section_presenter_interface import SectionPresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import \
    INVALID_SECTION_ID


class SectionPresenterImplementation(SectionPresenterInterface):

    def raise_invalid_section_id_exception(self):
        raise NotFound(*INVALID_SECTION_ID)
