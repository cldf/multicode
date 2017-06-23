# *-* coding: utf-8 *-*
from __future__ import print_function, division, unicode_literals
from unittest import TestCase

from multicode import ipa


class Tests(TestCase):
    def test_ipa_confusables(self):
        ic = ipa.ipa_confusables()
        self.assertEqual(ic['ɂ'], 'ʔ')

    def test_basic_confusables(self):
        bc = ipa.basic_confusables()
        self.assertEqual(bc['\u200A'], '"')
