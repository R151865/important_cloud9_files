import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.section_presenter_implementation \
    import SectionPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_SECTION_ID


def test_raise_invalid_section_id_exception():

    # Arrange
    exception_messages = INVALID_SECTION_ID[0]
    exception_res_status = INVALID_SECTION_ID[1]
    presenter = SectionPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_section_id_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
