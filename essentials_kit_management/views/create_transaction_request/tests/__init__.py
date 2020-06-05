# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "create_transaction_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "users/transcactions/request/"

from .test_case_01 import TestCase01CreateTransactionRequestAPITestCase

__all__ = [
    "TestCase01CreateTransactionRequestAPITestCase"
]
