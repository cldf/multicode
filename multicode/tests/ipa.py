# *-* coding: utf-8 *-*
from __future__ import print_function, division, unicode_literals
from multicode.ipa import ipa_confusables, basic_confusables


def test_ipa_confusables():
    ic = ipa_confusables()
    assert ic['ɂ'] == 'ʔ'

def test_basic_confusables():
    bc = basic_confusables()
    assert bc['\u200A'] == ' '
