# *-* coding: utf-8 *-*
from __future__ import unicode_literals, print_function, division

from multicode.util import data_path, load_yaml


def ipa_confusables():

    return load_yaml('confusables', 'ipa.yaml', revert=True)

def basic_confusables():
    return load_yaml('confusables', 'basic.yaml', revert=True)
