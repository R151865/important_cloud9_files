import pytest

from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface
from essentials_kit_management.interactors.storages import \
    FormStorageInterface

from essentials_kit_management.interactors. \
    get_user_ordered_details_interactor import GetUserOrderedDetailsInteractor

from essentials_kit_management.interactors.storages.dtos import (
    GetUserOrderDto
)


def test_get_user_ordered_details_interactor_with_valid_details(
        get_user_brand_dtos,
        get_user_items_dtos,
        get_user_order_dtos,
        get_expected_get_user_order_dtos
):

    # Arrange
    user_id = 1
    form_id = 1
    expected_dict = {}
    form_presenter = create_autospec(FormPresenterInterface)
    form_storage = create_autospec(FormStorageInterface)
    interactor = GetUserOrderedDetailsInteractor(form_storage=form_storage,
                                                 form_presenter=form_presenter)

    form_storage.get_order_dtos.return_value = get_user_order_dtos
    form_storage.get_user_brand_dtos.return_value = get_user_brand_dtos
    form_storage.get_user_item_dtos.return_value = get_user_items_dtos

    # Act
    actual_dict = interactor.get_user_ordered_details(user_id=user_id,
                                                      form_id=form_id)

    # Assert
    form_storage.is_valid_form_id(form_id=form_id)
    form_storage.get_order_dtos.assert_called_once_with(user_id=user_id,
                                                        form_id=form_id)
    form_storage.get_user_brand_dtos.assert_called_once()
    form_storage.get_user_item_dtos.assert_called_once()
    form_presenter.get_user_ordered_details_response(
         order_detail_dtos=get_expected_get_user_order_dtos)
