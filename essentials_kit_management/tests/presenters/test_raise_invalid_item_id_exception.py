import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.item_presenter_implementation \
    import ItemPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_ITEM_ID


def test_raise_invalid_item_id_exception():

    # Arrange
    exception_messages = INVALID_ITEM_ID[0]
    exception_res_status = INVALID_ITEM_ID[1]
    presenter = ItemPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_item_id_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
