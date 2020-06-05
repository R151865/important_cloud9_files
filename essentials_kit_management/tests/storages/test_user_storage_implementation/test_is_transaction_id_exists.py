import pytest

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
def test_is_transaction_id_exists_with_existed_transaction_id_return_true(
        create_users,
        create_transactions):

    # Arrange
    transaction_id = 111111
    storage = UserStorageImplementation()

    # Act
    is_transaction_already_exists = storage.is_transaction_id_exists(
        transaction_id=transaction_id)

    # Assert
    assert is_transaction_already_exists is True


@pytest.mark.django_db
def test_is_transaction_id_exists_with_not_existed_transaction_id_return_false(
        create_users,
        create_transactions):

    # Arrange
    transaction_id = 11111111111
    storage = UserStorageImplementation()

    # Act
    is_transaction_already_exists = storage.is_transaction_id_exists(
        transaction_id=transaction_id)

    # Assert
    assert is_transaction_already_exists is False