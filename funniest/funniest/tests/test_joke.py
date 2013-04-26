## This document is licensed under `CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/>`
## (C) 2013, Scott Torberg

from unittest import TestCase

import funniest


class TestJoke(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))
