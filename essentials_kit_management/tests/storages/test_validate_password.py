import pytest

from essentials_kit_management.models import User

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation
from essentials_kit_management.exceptions.exceptions import InvalidPassword


@pytest.mark.django_db
def test_validate_password_with_invalid_details(create_users):

    # Arrange
    invalid_password = "sulthan123345"
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        storage.validate_password(password=invalid_password)


@pytest.mark.django_db
def test_validate_password_with_valid_details(create_users):

    # Arrange
    password = "sulthan123"
    storage = UserStorageImplementation()

    # Act
    storage.validate_password(password=password)

    # Assert
    is_valid_password = User.objects.filter(password=password).exists()

    assert is_valid_password is True
