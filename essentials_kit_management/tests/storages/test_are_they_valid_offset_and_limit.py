from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation


def test_are_they_valid_offset_and_limit_with_invalid_limit_return_false():

    # Arrange
    offset = 0
    limit = 0
    storage = FormStorageImplementation()

    # Act
    are_they_valid_offset_and_limit = storage.are_they_valid_offset_and_limit(
        offset=offset,
        limit=limit)

    # Assert
    assert are_they_valid_offset_and_limit is False


def test_are_they_valid_offset_and_limit_with_valid_details_return_true():

    # Arrange
    offset = 0
    limit = 2
    storage = FormStorageImplementation()

    # Act
    are_they_valid_offset_and_limit = storage.are_they_valid_offset_and_limit(
        offset=offset,
        limit=limit)

    # Assert
    assert are_they_valid_offset_and_limit is True


def test_are_they_valid_offset_and_limit_with_invalid_offset_return_true():

    # Arrange
    offset = -1
    limit = 2
    storage = FormStorageImplementation()

    # Act
    are_they_valid_offset_and_limit = storage.are_they_valid_offset_and_limit(
        offset=offset,
        limit=limit)

    # Assert
    assert are_they_valid_offset_and_limit is False


def test_are_they_valid_offset_and_limit_with_invalid_details_return_true():

    # Arrange
    offset = -1
    limit = 0
    storage = FormStorageImplementation()

    # Act
    are_they_valid_offset_and_limit = storage.are_they_valid_offset_and_limit(
        offset=offset,
        limit=limit)

    # Assert
    assert are_they_valid_offset_and_limit is False