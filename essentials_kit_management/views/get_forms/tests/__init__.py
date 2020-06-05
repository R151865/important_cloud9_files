# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_forms"
REQUEST_METHOD = "get"
URL_SUFFIX = "forms/"

from .test_case_01 import TestCase01GetFormsAPITestCase

__all__ = [
    "TestCase01GetFormsAPITestCase"
]
