import pytest

from essentials_kit_management.presenters.form_presenter_implementation \
    import FormPresenterImplementation

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import \
    INVALID_FORM_ID


def test_raise_invalid_form_id_exception_with_invalid_form_id():

    # Arrange
    exception_message =  INVALID_FORM_ID[0]
    exception_res_status = INVALID_FORM_ID[1]
    form_presenter = FormPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        form_presenter.raise_invalid_form_id_exception()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
