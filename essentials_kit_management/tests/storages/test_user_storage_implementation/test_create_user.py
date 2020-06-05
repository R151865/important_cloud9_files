import pytest

from essentials_kit_management.models import User

from essentials_kit_management.storages.user_storage_implementation \
    import UserStorageImplementation


@pytest.mark.django_db
def test_create_user_with_valid_details():

    # Arrange
    name = "Sulthan"
    username = "12456788"
    password = "sulthi123"
    storage = UserStorageImplementation()

    # Act
    new_user_id = storage.create_user(name=name,
                                      username=username,
                                      password=password)

    # Assert
    user_obj = User.objects.get(id=new_user_id)

    assert user_obj.id == new_user_id
    assert user_obj.name == name
    assert user_obj.username == username
    assert user_obj.password == password