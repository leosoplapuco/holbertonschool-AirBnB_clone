#!/usr/bin/python3
"""test review"""

from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.review import Review


class TestCity(TestCase):
    """TestCity"""
    def test_9(self):
        """test_9"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')
