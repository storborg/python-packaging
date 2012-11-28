from unittest import TestCase

from funniest.cmd import main


class TestCmd(TestCase):
    def test_basic(self):
        main()
