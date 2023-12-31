#!/usr/bin/python3
"""test BaseModel"""

import unittest
from datetime import datetime
from models.base_models import BaseModel

class TestBaseModel(unittest.TestCase):
    """TestBaseModel"""

    def setUp(self):
        self.testbasemodel = BaseModel()

    def test_pep8_BaseModel(self):
        """test_pep8_BaseModel"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")


    def test_save_BaesModel(self):
        """test_save_Basemodel"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_doc(self):
        """test_doc"""
        self.assertisNotNone(BaseModel.__doc__)

    def test_to_json(self):
        """test_to_json"""

    def test_kwarg(self):
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

if __name__ == "__main__":
    unittest.main()
