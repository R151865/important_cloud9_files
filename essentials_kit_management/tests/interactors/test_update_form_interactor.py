import pytest

from unittest.mock import create_autospec

from essentials_kit_management.interactors.storages.form_storage_interface \
     import FormStorageInterface
from essentials_kit_management.interactors.presenters. \
    form_presenter_interface import FormPresenterInterface
from essentials_kit_management.interactors.storages. \
    section_storage_interface import SectionStorageInterface
from essentials_kit_management.interactors.presenters. \
    section_presenter_interface import SectionPresenterInterface

from essentials_kit_management.interactors.storages.item_storage_interface \
     import ItemStorageInterface
from essentials_kit_management.interactors.presenters. \
    item_presenter_interface import ItemPresenterInterface
from essentials_kit_management.interactors.storages.brand_storage_interface \
     import BrandStorageInterface
from essentials_kit_management.interactors.presenters. \
    brand_presenter_interface import BrandPresenterInterface


from essentials_kit_management.interactors.storages.order_storage_interface \
     import OrderStorageInterface
from essentials_kit_management.interactors.presenters. \
    order_presenter_interface import OrderPresenterInterface

from essentials_kit_management.interactors.update_form_interactor import \
    UpdateFormInteractor


def test_update_form_interactor_with_valid_details_update_orders(
        update_form_order_dict,
        expected_update_form_dto_list):

    # Arrange
    user_id = 1
    form_id = 1
    new_order_list = expected_update_form_dto_list[0]
    update_order_list = expected_update_form_dto_list[1]
    remove_order_list = expected_update_form_dto_list[2]

    order_storage = create_autospec(OrderStorageInterface)
    order_presenter = create_autospec(OrderPresenterInterface)
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    section_storage = create_autospec(SectionStorageInterface)
    section_presenter = create_autospec(SectionPresenterInterface)
    item_storage = create_autospec(ItemStorageInterface)
    item_presenter = create_autospec(ItemPresenterInterface)
    brand_storage = create_autospec(BrandStorageInterface)
    brand_presenter = create_autospec(BrandPresenterInterface)

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

    # Act
    interactor.update_form(user_id=user_id,
                           orders_details=update_form_order_dict)

    # Assert
    form_storage.is_valid_form_id.assert_called_once_with(form_id=form_id)
    assert order_storage.create_new_orders(user_id=user_id,
                                           new_order_list=new_order_list)
    assert order_storage.update_orders(update_order_list=update_order_list)
    assert order_storage.remove_orders(remove_order_list=remove_order_list)
