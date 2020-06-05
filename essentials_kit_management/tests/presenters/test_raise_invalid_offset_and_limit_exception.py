import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_OFFSET_LENGTH


def test_raise_invalid_offset_and_limit_exception():

    # Arrange
    exception_messages = INVALID_OFFSET_LENGTH[0]
    exception_res_status = INVALID_OFFSET_LENGTH[1]
    presenter = FormPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_offset_and_limit_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
