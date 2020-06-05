import pytest

from essentials_kit_management.models import User

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation
from essentials_kit_management.exceptions.exceptions import InvalidUsername


@pytest.mark.django_db
def test_validate_username_with_invalid_details(create_users):

    # Arrange
    invalid_username = 98765
    password = "sulthan123"
    storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUsername):
        storage.validate_username(username=invalid_username,
                                  password=password)


@pytest.mark.django_db
def test_validate_username_with_valid_details_return_user_id(create_users):
 
    # Arrange
    username = "9876543214"
    password = "anju123"
    storage = UserStorageImplementation()

    # Act
    actual_user_id = storage.validate_username(username=username,
                                               password=password)

    # Assert
    user_obj = User.objects.get(id=actual_user_id)
    
    user_id = user_obj.id

    assert actual_user_id == user_id
    assert user_obj.username == username
    assert user_obj.password == password