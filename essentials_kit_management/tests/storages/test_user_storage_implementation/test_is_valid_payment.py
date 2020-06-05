from essentials_kit_management.storages.user_storage_implementation \
    import UserStorageImplementation


def test_is_valid_payment_with_invalid_payment_return_false():

    # Arrange
    invalid_payment = -10
    storage = UserStorageImplementation()

    # Act
    is_valid_payment = storage.is_valid_payment(amount=invalid_payment)

    # Assert
    assert is_valid_payment is False


def test_is_valid_payment_with_valid_payment_return_true():

    # Arrange
    invalid_payment = 100
    storage = UserStorageImplementation()

    # Act
    is_valid_payment = storage.is_valid_payment(amount=invalid_payment)

    # Assert
    assert is_valid_payment is True


def test_is_valid_payment_with_zero_payment_return_false():

    # Arrange
    invalid_payment = 0
    storage = UserStorageImplementation()

    # Act
    is_valid_payment = storage.is_valid_payment(amount=invalid_payment)

    # Assert
    assert is_valid_payment is False
