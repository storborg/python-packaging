from unittest import TestCase

import funniest


class TestJoke(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))
