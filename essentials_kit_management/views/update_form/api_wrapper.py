import json

from django.http import HttpResponse

from essentials_kit_management.storages.form_storage_implementation \
     import FormStorageImplementation
from essentials_kit_management.presenters.form_presenter_implementation \
     import FormPresenterImplementation
from essentials_kit_management.storages.section_storage_implementation \
     import SectionStorageImplementation
from essentials_kit_management.presenters.section_presenter_implementation \
     import SectionPresenterImplementation

from essentials_kit_management.storages.item_storage_implementation \
     import ItemStorageImplementation
from essentials_kit_management.presenters.item_presenter_implementation \
     import ItemPresenterImplementation
from essentials_kit_management.storages.brand_storage_implementation \
     import BrandStorageImplementation
from essentials_kit_management.presenters.brand_presenter_implementation \
     import BrandPresenterImplementation

from essentials_kit_management.storages.order_storage_implementation \
     import OrderStorageImplementation
from essentials_kit_management.presenters.order_presenter_implementation \
     import OrderPresenterImplementation

from essentials_kit_management.interactors.update_form_interactor import \
    UpdateFormInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    print("1***********")
    user = kwargs["user"]
    user_id = user.id

    request_data = kwargs["request_data"]


    order_storage = OrderStorageImplementation()
    order_presenter = OrderPresenterImplementation()
    form_storage = FormStorageImplementation()
    form_presenter = FormPresenterImplementation()
    section_storage = SectionStorageImplementation()
    section_presenter = SectionPresenterImplementation()
    item_storage = ItemStorageImplementation()
    item_presenter = ItemPresenterImplementation()
    brand_storage = BrandStorageImplementation()
    brand_presenter = BrandPresenterImplementation()

    interactor = UpdateFormInteractor(
        order_storage=order_storage,
        order_presenter=order_presenter,
        form_storage=form_storage,
        form_presenter=form_presenter,
        section_storage=section_storage,
        section_presenter=section_presenter,
        item_storage=item_storage,
        item_presenter=item_presenter,
        brand_storage=brand_storage,
        brand_presenter=brand_presenter)

    interactor.update_form(user_id=user_id,
                           orders_details=request_data)

    response = HttpResponse()

    return response