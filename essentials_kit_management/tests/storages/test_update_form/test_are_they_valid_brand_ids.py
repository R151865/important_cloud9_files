import pytest

from essentials_kit_management.storages.brand_storage_implementation \
    import BrandStorageImplementation

from essentials_kit_management.models import Brand

@pytest.mark.django_db
def test_are_they_valid_brand_ids_with_invalid_brand_ids_return_false(
        populate_data):

    # Arrange
    invalid_brand_ids = [1, 2, -1]
    brand_storage = BrandStorageImplementation()

    # Act
    are_they_valid_brand_ids = brand_storage.are_they_valid_brand_ids(
        brand_ids=invalid_brand_ids)

    # Assert
    assert are_they_valid_brand_ids is False


@pytest.mark.django_db
def test_are_they_valid_brand_ids_with_valid_brand_ids_return_true(
        populate_data):

    # Arrange
    brand_ids = [1, 2, 3]
    brand_storage = BrandStorageImplementation()

    # Act
    are_they_valid_brand_ids = brand_storage.are_they_valid_brand_ids(
        brand_ids=brand_ids)

    # Assert
    assert are_they_valid_brand_ids is True