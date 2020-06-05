import pytest

from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation


def test_get_form_response_with_valid_details_return_dict(
        get_form_details_dto,
        get_form_expected_dict):

    # Arrange
    expected_dict =  get_form_expected_dict
    form_presenter = FormPresenterImplementation()

    # Act
    actual_dict = form_presenter.get_form_response(get_form_details_dto)

    # Assert
    assert actual_dict == expected_dict
