import json

from django.http import HttpResponse

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation

from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation
from essentials_kit_management. \
    interactors.get_admin_account_details_interactor import \
        GetAdminAccountDetailsInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_storage = UserStorageImplementation()
    user_presenter = UserPresenterImplementation()
    interactor = GetAdminAccountDetailsInteractor(
        user_storage=user_storage,
        user_presenter=user_presenter)

    upi_id_dict = interactor.get_admin_account_details()

    upi_id_dict_json = json.dumps(upi_id_dict)
    response_data = HttpResponse(upi_id_dict_json, status=200)

    return response_data
