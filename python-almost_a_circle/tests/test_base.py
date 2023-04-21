#!/usr/bin/python3
""" test_base.py """


import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base """
    
    def test_base(self):
        b1 = Base()
        b2 = Base()
        b9 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b9.id, 89)
        self.assertEqual(b3.id, 3)

unittest.main()