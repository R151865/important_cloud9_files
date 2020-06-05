import pytest
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_PAYMENT

from django_swagger_utils.drf_server.exceptions import NotFound

def test_raise_invalid_payment_exception():

    # Arrange
    exception_message =  INVALID_PAYMENT[0]
    exception_res_status = INVALID_PAYMENT[1]
    user_presenter = UserPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        user_presenter.raise_invalid_payment_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status