#!/usr/bin/python3
"""test file storage"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """TestFileStorage"""

    def test_pep8_FileStorage(self):
        """test_pep8_FileStorage"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")



if __name__ == "__main__":
    unittest.main()
