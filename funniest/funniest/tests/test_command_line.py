## This document is licensed under `CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/>`
## (C) 2013, Scott Torberg

from unittest import TestCase

from funniest.cmd import main


class TestCmd(TestCase):
    def test_basic(self):
        main()
