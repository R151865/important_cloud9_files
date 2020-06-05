import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    TRANSACTION_ID_ALREADY_EXISTS


def test_raise_transaction_id_already_exists_exception():

    # Arrange
    exception_messages = TRANSACTION_ID_ALREADY_EXISTS[0]
    exception_res_status = TRANSACTION_ID_ALREADY_EXISTS[1]
    presenter = UserPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_transaction_id_already_exist_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
