# *-* coding: utf-8 *-*
from __future__ import unicode_literals, print_function, division
from functools import partial

from multicode.util import load


ipa_confusables = partial(load, 'confusables', table_name='ipa.tsv')
epa_confusables = partial(load, 'confusables', table_name='epa.tsv')
basic_confusables = partial(load, 'confusables', table_name='basic.tsv')
