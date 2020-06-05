import json

from django.http import HttpResponse

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation
from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation

from essentials_kit_management.interactors.get_user_ordered_details_interactor \
    import GetUserOrderedDetailsInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs["user"]
    user_id = user.id
    form_id = kwargs["form_id"]

    form_storage = FormStorageImplementation()
    form_presenter = FormPresenterImplementation()
    interactor = GetUserOrderedDetailsInteractor(form_storage=form_storage,
                                                 form_presenter=form_presenter)

    user_ordered_details_list = interactor.get_user_ordered_details(
        user_id=user_id,
        form_id=form_id)

    user_ordered_details_list_json = json.dumps(user_ordered_details_list)
    response_data = HttpResponse(user_ordered_details_list_json, status=200)

    return response_data
