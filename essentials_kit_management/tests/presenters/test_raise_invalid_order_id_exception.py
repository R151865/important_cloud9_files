import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.order_presenter_implementation \
    import OrderPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_ORDER_ID


def test_raise_invalid_order_id_exception():

    # Arrange
    exception_messages = INVALID_ORDER_ID[0]
    exception_res_status = INVALID_ORDER_ID[1]
    presenter = OrderPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_order_id_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
