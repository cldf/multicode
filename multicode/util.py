# coding: utf8
from __future__ import unicode_literals, print_function, division
import re

from six import unichr
from clldutils.path import Path
from clldutils.csvw.metadata import TableGroup

import multicode

CODE_POINT_PATTERN = re.compile('U\+[0-9a-fA-F]{4}$')


def data_path(*comps):
    return Path(multicode.__file__).parent.joinpath('data', *comps)


def char(spec):
    if CODE_POINT_PATTERN.match(spec):
        return unichr(int(spec.replace('U+', '0x'), base=16))
    return spec


def load(name, table_name=None):
    tg = TableGroup.from_file(data_path(name, 'metadata.json'))
    res = {}
    for table in tg.tables:
        if table_name is None or table.local_name == table_name:
            for row in table:
                if row:
                    for alias in row['alias']:
                        res[char(alias)] = char(row['char'])
    return res
