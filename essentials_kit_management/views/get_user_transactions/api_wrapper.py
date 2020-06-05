import json

from django.http import HttpResponse

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.interactors.get_user_transactions_interactor \
    import GetUserTransactionsInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs["user"]
    user_id = user.id

    user_storage = UserStorageImplementation()
    user_presenter = UserPresenterImplementation()
    interactor = GetUserTransactionsInteractor(user_storage=user_storage,
                                               user_presenter=user_presenter)

    transaction_details_dict = interactor.get_user_transactions(
        user_id=user_id)

    transaction_details_dict_json = json.dumps(transaction_details_dict)
    response_data = HttpResponse(transaction_details_dict_json, status=200)

    return response_data

