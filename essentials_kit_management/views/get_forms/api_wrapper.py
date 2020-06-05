import json

from django.http import HttpResponse

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.presenters.form_presenter_implementation import \
    FormPresenterImplementation
from essentials_kit_management.interactors.get_forms_interactor import \
    GetFormsInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id

    offset = kwargs["request_query_params"]["offset"]
    limit = kwargs["request_query_params"]["limit"]

    form_storage = FormStorageImplementation()
    form_presenter = FormPresenterImplementation()
    interactor = GetFormsInteractor(form_storage=form_storage,
                                    form_presenter=form_presenter)


    forms_dict_list = interactor.get_forms(user_id=user_id,
                                           offset=offset,
                                           limit=limit)
    
    forms_dict_list_json = json.dumps(forms_dict_list)
    response = HttpResponse(forms_dict_list_json, status=200)

    return response
