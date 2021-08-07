from segments import Tokenizer, Profile

from multicode.util import iteraliases

__version__ = "0.2.1"

SPACE = '<-SPACE->'
NEWLINE = '<-NEWLINE->'
ipa_confusables = dict(iteraliases('confusables', table_name='ipa.tsv'))
epa_confusables = dict(iteraliases('confusables', table_name='epa.tsv'))
basic_confusables = dict(iteraliases('confusables', table_name='basic.tsv'))


def _orthography_profile(s):
    graphemes = {c: c for c in s}
    graphemes[NEWLINE] = '\n'
    graphemes.update(basic_confusables)
    graphemes.update(epa_confusables)
    graphemes.update(ipa_confusables)
    return Profile(*(
        {'Grapheme': k, 'IPA': SPACE if v == ' ' else v} for k, v in graphemes.items()))


def recode(s):
    t = Tokenizer(profile=_orthography_profile(s))
    return t(
        s.replace('\n', NEWLINE),
        column='IPA',
        segment_separator='',
        separator=' ').replace(SPACE, ' ')
