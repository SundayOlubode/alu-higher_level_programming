#!/usr/bin/python3
""" test_base.py """


import os
from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """ Test Base class """
    def test_base(self):
        base_1 = Base()
        base_2 = Base()
        base_89 = Base(89)
        base_3 = Base()
        self.assertEqual(1, base_1.id)
        self.assertEqual(2, base_2.id)
        self.assertEqual(89, base_89.id)
        self.assertEqual(3, base_3.id)
