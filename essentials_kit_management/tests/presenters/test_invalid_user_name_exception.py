import pytest
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_USER_NAME

from django_swagger_utils.drf_server.exceptions import NotFound


def test_invalid_user_name_exception():

    # Arrange
    exception_message = INVALID_USER_NAME[0]
    exception_res_status = INVALID_USER_NAME[1]
    user_presenter = UserPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        user_presenter.raise_invalid_username_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status