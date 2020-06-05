import json

from django.http import HttpResponse

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation

from essentials_kit_management.presenters.user_presenter_implementation import \
    UserPresenterImplementation
from essentials_kit_management.interactors.create_user_signup_interactor \
    import CreateUserSignUpInteractor

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs["request_data"]
    name = request_data["name"]
    username = request_data["username"]
    password = request_data["password"]

    user_storage = UserStorageImplementation()
    user_presenter = UserPresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = CreateUserSignUpInteractor(user_storage=user_storage,
                                            user_presenter=user_presenter,
                                            oauth2_storage=oauth2_storage)

    access_tocken_dict = interactor.create_signup(name=name,
                                                  username=username,
                                                  password=password)

    access_tocken_dict_json = json.dumps(access_tocken_dict)
    response_data = HttpResponse(access_tocken_dict_json, status=201)

    return response_data