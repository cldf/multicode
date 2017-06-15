import os
import yaml
import codecs

def data_path(*comps):
    """
    Our data-path in CLICS.
    """
    return os.path.join(os.path.dirname(__file__), os.pardir, 'data', *comps)


def load_yaml(*paths, revert=False):
    with codecs.open(data_path(*paths), 'r', 'utf-8') as f:
        data = yaml.load(f)
    if not revert:
        return data
    return revert_dictionary(data)

def revert_dictionary(dictionary):
    out = {}
    for key, values in dictionary.items():
        for value in values:
            out[value] = key
    return out



