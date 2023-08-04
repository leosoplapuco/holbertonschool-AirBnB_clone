#!/usr/bin/python3
"""módulo test para User"""
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.user import User


class TestUser(TestCase):
    """TestUser"""
    def test_8(self):
        """test_8"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')
