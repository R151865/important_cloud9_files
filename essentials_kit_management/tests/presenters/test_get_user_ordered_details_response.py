from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation


def test_get_user_ordered_details_response(
        get_user_ordered_details_dto_and_expected_dict):

    # Arrange
    ordered_details_dtos = get_user_ordered_details_dto_and_expected_dict[0]
    expected_dict_list = get_user_ordered_details_dto_and_expected_dict[1]
    form_presenter = FormPresenterImplementation()

    # Act
    actual_dict_list = form_presenter.get_user_ordered_details_response(
        ordered_details_dtos)

    # Assert
    assert actual_dict_list == expected_dict_list