import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface
from essentials_kit_management.interactors.storages import \
    FormStorageInterface

from essentials_kit_management.interactors.get_forms_interactor import \
    GetFormsInteractor

from essentials_kit_management.interactors.storages.dtos import (
    HomePageFormDto, FormCompleteDetailsDto
)


def test_get_forms_interactors_with_valid_details(brand_dtos,
                                                  items_dtos,
                                                  order_dtos,
                                                  form_dtos,
                                                  get_expected_form_dtos):

    # Arrange
    user_id = 1
    offset = 0
    limit = 50
    total_forms_count = 100
    expected_forms_dict_list = []
    form_with_details_dto1 = FormCompleteDetailsDto(
        item_dtos=items_dtos,
        order_dtos=order_dtos,
        form_dto=form_dtos[0],
        brand_dtos=brand_dtos)

    form_complete_details_dtos = \
        [form_with_details_dto1, form_with_details_dto1]
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormsInteractor(form_storage=form_storage,
                                    form_presenter=form_presenter)

    form_storage.get_forms_dtos.return_value = form_dtos, total_forms_count
    form_storage.get_user_order_dtos.return_value = order_dtos
    form_storage.get_user_brand_dtos.return_value = brand_dtos
    form_storage.get_user_item_dtos.return_value = items_dtos

    form_presenter.get_forms_response.return_value = expected_forms_dict_list

    # Act
    actual_forms_dict_list = interactor.get_forms(user_id=user_id,
                                                  offset=offset,
                                                  limit=limit)

    # Assert
    form_storage.are_they_valid_offset_and_limit.assert_called_once_with(
        offset=offset, limit=limit)
    form_presenter.get_forms_response.assert_called_once_with(
        form_dtos=get_expected_form_dtos, total_forms_count=total_forms_count)
    form_storage.get_forms_dtos.assert_called_once_with(offset=offset,
                                                        limit=limit)


def test_get_forms_interactors_with_valid_details_with_invalid_offset_and_limit(
        ):

    # Arrange
    user_id = 1
    offset = 0
    limit = -1
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormsInteractor(form_storage=form_storage,
                                    form_presenter=form_presenter)

    form_storage.are_they_valid_offset_and_limit.return_value = False
    form_presenter.raise_invalid_offset_and_limit_exception.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_forms(user_id=user_id,
                             offset=offset,
                             limit=limit)
