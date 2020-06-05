import pytest

from unittest.mock import create_autospec

from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface
from essentials_kit_management.interactors.storages import \
    FormStorageInterface

from essentials_kit_management.interactors.get_form_to_fill_interactor import \
    GetFormToFillInteractor

from essentials_kit_management.exceptions.exceptions import InvalidFormId


def test_get_form_to_fill_interactors_with_valid_details():

    # Arrange
    form_id = 1
    expected_form_dict = []
    form_dto = "form_dto"
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormToFillInteractor(form_storage=form_storage,
                                         form_presenter=form_presenter)

    form_storage.get_form_to_fill_dto.return_value = form_dto
    form_presenter.get_form_to_fill_response.return_value = expected_form_dict

    # Act
    actual_form_dict = interactor.get_form_to_fill(form_id=form_id)

    # Assert
    form_storage.is_valid_form_id.assert_called_once_with(form_id=form_id)
    form_storage.get_form_to_fill_dto.assert_called_once_with(form_id=form_id)
    form_presenter.get_form_to_fill_response.assert_called_once_with(
        form_dto=form_dto)
    assert actual_form_dict == expected_form_dict

def test_get_form_to_fill_interactors_with_invalid_form_id_raise_exception():

    # Arrange
    invalid_form_id = -1
    form_storage = create_autospec(FormStorageInterface)
    form_presenter = create_autospec(FormPresenterInterface)
    interactor = GetFormToFillInteractor(form_storage=form_storage,
                                         form_presenter=form_presenter)

    form_storage.is_valid_form_id.return_value = False
    form_presenter.raise_invalid_form_id_exception.side_effect = InvalidFormId

    # Act
    with pytest.raises(InvalidFormId):
        interactor.get_form_to_fill(form_id=invalid_form_id)
