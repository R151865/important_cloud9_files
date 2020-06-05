import json

from django.http import HttpResponse

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.presenters.form_presenter_implementation import \
    FormPresenterImplementation
from essentials_kit_management.interactors.get_form_interactor import \
    GetFormInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    user = kwargs['user']
    user_id = user.id
    form_id = kwargs["form_id"]
    
    form_storage = FormStorageImplementation()
    form_presenter = FormPresenterImplementation()
    interactor = GetFormInteractor(form_storage=form_storage,
                                   form_presenter=form_presenter)

    form_details_dict = interactor.get_form(form_id=form_id,
                                                user_id=user_id)
    
    form_details_dict_json = json.dumps(form_details_dict)
    response = HttpResponse(form_details_dict_json, status=200)

    return response
