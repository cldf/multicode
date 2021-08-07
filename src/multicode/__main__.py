import sys

from clldutils.clilib import ArgumentParser, command
from multicode import recode


@command(name='recode')
def _recode(args):
    """
    Replace all confusables in input string with the canonical character.
    """
    in_ = args.args[0] if args.args else sys.stdin.read()
    sys.stdout.write(recode(in_))
    sys.stdout.write('\n')


def main():  # pragma: no cover
    parser = ArgumentParser('multicode')
    sys.exit(parser.main())


if __name__ == '__main__':  # pragma: no cover
    main()
