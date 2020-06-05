# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "create_sections"
REQUEST_METHOD = "post"
URL_SUFFIX = "forms/sections/create/"

from .test_case_01 import TestCase01CreateSectionsAPITestCase

__all__ = [
    "TestCase01CreateSectionsAPITestCase"
]
