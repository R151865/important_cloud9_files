import pytest

from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation


def test_get_forms_response_with_valid_details_return_dict(
        get_forms_response_list,
        get_forms_expected_dict):

    # Arrange
    total_forms_count = 100
    expected_dict =  get_forms_expected_dict
    form_presenter = FormPresenterImplementation()

    # Act
    actual_dict = form_presenter.get_forms_response(
        get_forms_response_list, total_forms_count)

    # Assert
    assert actual_dict == expected_dict