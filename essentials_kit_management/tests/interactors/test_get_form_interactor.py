import pytest

from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface
from essentials_kit_management.interactors.storages import \
    FormStorageInterface

from essentials_kit_management.interactors.get_form_interactor import \
    GetFormInteractor

from essentials_kit_management.interactors.storages.dtos import (
    HomePageFormDto, FormCompleteDetailsDto
)



def test_get_form_interactors_with_valid_details(
        get_form_dto,
        get_form_order_dtos,
        get_form_brand_dtos,
        get_form_items_dtos,
        get_form_section_dtos,
        get_form_expected_form_details_dto):
 
    # Arrange
    user_id = 1
    form_id = 1

    expected_dict = []
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormInteractor(form_storage=form_storage,
                                  form_presenter=form_presenter)


    form_storage.get_form_dto.return_value = get_form_dto
    form_storage.get_order_dtos.return_value = get_form_order_dtos
    form_storage.get_form_sections_dtos.return_value = get_form_section_dtos
    form_storage.get_item_dtos.return_value = get_form_items_dtos
    form_storage.get_brand_dtos.return_value = get_form_brand_dtos


    form_presenter.get_form_response.return_value = expected_dict

    # Act
    actual_dict = interactor.get_form(user_id=user_id,
                                      form_id=form_id)

    # Assert
    assert actual_dict == expected_dict
    form_presenter.get_form_response.assert_called_once_with(
        get_form_details_dto=get_form_expected_form_details_dto
    )
    form_storage.is_valid_form_id.assert_called_once_with(form_id=form_id)
    form_storage.get_form_dto.assert_called_once_with(form_id=form_id)
    form_storage.get_order_dtos.assert_called_once_with(user_id=user_id,
                                                        form_id=form_id)
    form_storage.get_form_sections_dtos.assert_called_once_with(form_id=form_id)
    form_storage.get_item_dtos.assert_called_once_with(
        section_dtos=get_form_section_dtos)
    form_storage.get_brand_dtos.assert_called_once_with(
        item_dtos=get_form_items_dtos)


def test_get_form_interactors_with_invalid_form_id_raise_exception():

    # Arrange
    user_id = 1
    invalid_form_id = 1

    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormInteractor(form_storage=form_storage,
                                  form_presenter=form_presenter)

    form_storage.is_valid_form_id.return_value = False
    form_presenter.raise_invalid_form_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_form(user_id=user_id,
                            form_id=invalid_form_id)