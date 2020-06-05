# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "create_form"
REQUEST_METHOD = "post"
URL_SUFFIX = "forms/create/"

from .test_case_01 import TestCase01CreateFormAPITestCase

__all__ = [
    "TestCase01CreateFormAPITestCase"
]
