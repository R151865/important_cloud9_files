import pytest
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    USERNAME_ARLEADY_EXISTS

from django_swagger_utils.drf_server.exceptions import Forbidden


def test_raise_username_already_exists_exception():

    # Arrange
    exception_message = USERNAME_ARLEADY_EXISTS[0]
    exception_res_status = USERNAME_ARLEADY_EXISTS[1]
    user_presenter = UserPresenterImplementation()

    # Act
    with pytest.raises(Forbidden) as exception:
        user_presenter.raise_username_already_exists_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status