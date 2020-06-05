import pytest

from essentials_kit_management.storages.item_storage_implementation \
    import ItemStorageImplementation

from essentials_kit_management.models import Item

@pytest.mark.django_db
def test_are_they_valid_item_ids_with_invalid_item_ids_return_false(
        populate_data):

    # Arrange
    invalid_item_ids = [1, 2, -1]
    item_storage = ItemStorageImplementation()

    # Act
    are_they_valid_item_ids = item_storage.are_they_valid_item_ids(
        item_ids=invalid_item_ids)

    # Assert
    assert are_they_valid_item_ids is False


@pytest.mark.django_db
def test_are_they_valid_item_ids_with_valid_item_ids_return_true(
        populate_data):

    # Arrange
    item_ids = [1, 2, 3]
    item_storage = ItemStorageImplementation()

    # Act
    are_they_valid_item_ids = item_storage.are_they_valid_item_ids(
        item_ids=item_ids)

    # Assert
    assert are_they_valid_item_ids is True