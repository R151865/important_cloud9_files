from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation


def test_get_upi_id_response():

    # Arrrange
    upi_id = "123456890@SBI"
    expected_upi_id_dict = {
        "upi_id": upi_id
    }
    storage = UserPresenterImplementation()

    # Act
    actual_upi_id_dict = storage.get_upi_id_response(upi_id=upi_id)

    # Assert
    assert actual_upi_id_dict == expected_upi_id_dict