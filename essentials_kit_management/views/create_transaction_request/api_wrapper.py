import json

from django.http import HttpResponse

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.interactors. \
    create_transaction_request_interactor import \
        CreateTransactionRequestInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs["user"]
    user_id = user.id
    transaction_dict = kwargs["request_data"]

    user_storage = UserStorageImplementation()
    user_presenter = UserPresenterImplementation()
    interactor = CreateTransactionRequestInteractor(
        user_storage=user_storage,
        user_presenter=user_presenter)

    interactor.create_transaction_request(user_id=user_id,
                                          transaction_dict=transaction_dict)

    response_data = HttpResponse(status=201)
    return response_data