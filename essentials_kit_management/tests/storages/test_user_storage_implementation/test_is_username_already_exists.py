import pytest

from essentials_kit_management.storages.user_storage_implementation \
    import UserStorageImplementation


@pytest.mark.django_db
def test_is_username_already_exists_with_existed_username_return_true(
        create_users):

    # Arrange
    existed_username = "9876543210"
    storage = UserStorageImplementation()

    # Act
    is_username_already_exists = storage.is_username_already_exists(
        username=existed_username)
    
    # Assert
    assert is_username_already_exists is True


@pytest.mark.django_db
def test_is_username_already_exists_with_not_existed_username_return_false(
        create_users):

    # Arrange
    not_existed_username = "00000000000"
    storage = UserStorageImplementation()

    # Act
    is_username_already_exists = storage.is_username_already_exists(
        username=not_existed_username)
    
    # Assert
    assert is_username_already_exists is False