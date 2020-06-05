import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.presenters.brand_presenter_implementation \
    import BrandPresenterImplementation

from essentials_kit_management.constants.exception_messages import \
    INVALID_BRAND_ID


def test_raise_invalid_brand_id_exception():

    # Arrange
    exception_messages = INVALID_BRAND_ID[0]
    exception_res_status = INVALID_BRAND_ID[1]
    presenter = BrandPresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_brand_id_exception()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
