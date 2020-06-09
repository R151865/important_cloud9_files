import datetime

from common.dtos import UserAuthTokensDTO

from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation


def test_get_access_token_response_with_valid_details_return_dto():

    # Arrange
    access_token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="QTRTUGFTTTBBBBNS1334",
        refresh_token="WQEDRTT#$%^REDET",
        expires_in=datetime.datetime(2020, 10, 10, 0, 0, 0))

    expected_access_token_dict = {
            "user_id": 1,
            "access_token": "QTRTUGFTTTBBBBNS1334",
            "refresh_token": "WQEDRTT#$%^REDET",
            "expires_in": "2020-10-10 00:00:00.000000"
        }
    user_presenter = UserPresenterImplementation()

    # Act
    actual_access_token_dict = user_presenter.get_access_token_response(
        access_token_dto)

    # Assert
    assert actual_access_token_dict == expected_access_token_dict
