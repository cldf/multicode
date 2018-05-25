# coding: utf8
from __future__ import unicode_literals, print_function, division
import sys

from clldutils.clilib import ArgumentParser, command
from multicode import recode


@command(name='recode')
def _recode(args):
    """
    Replace all confusables in input string with the canonical character.
    """
    sys.stdout.write(recode(args.args[0] + '\n'))


def main():  # pragma: no cover
    parser = ArgumentParser('multicode')
    sys.exit(parser.main())


if __name__ == '__main__':  # pragma: no cover
    main()
