#! /usr/bin/env python

'''
Tests for the Console UI
'''

import os
import sys

from unittest import TestCase
from console import rowcol_to_spot


class TestConsole(TestCase):
    def test_rowcol_to_spot(self):
        self.assertEquals(rowcol_to_spot('a1'),0)
        self.assertEquals(rowcol_to_spot('a2'),1)
        self.assertEquals(rowcol_to_spot('a3'),2)
        self.assertEquals(rowcol_to_spot('b1'),3)
        self.assertEquals(rowcol_to_spot('c1'),6)
        self.assertEquals(rowcol_to_spot('c3'),8)
