# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_user_transactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/transactions/"

from .test_case_01 import TestCase01GetUserTransactionsAPITestCase

__all__ = [
    "TestCase01GetUserTransactionsAPITestCase"
]
