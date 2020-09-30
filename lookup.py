import argparse
import sys

import repoindex

def main():
    try:
        print(repoindex.match(ARGS.checksum).url.strip())
    except ValueError:
        matches = repoindex.matches(ARGS.checksum)
        message = '%s values' % len(matches)
        sys.stderr.write(message + '\n')
        for match in matches:
            sys.stderr.write(repr(match) + '\n')


PARSER=argparse.ArgumentParser(
    prog='lookup',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=  "Return the URL of a git repo with given checksum as initial commit",
    epilog="""
Example:
    $ %(prog)s  3e7
    https://path.to.host/path/to/repo
    """,
)
PARSER.add_argument(
    'checksum',
    metavar='CHECKSUM',
    help='checksum of the initial commit',
    )

ARGS=PARSER.parse_args()


if __name__=='__main__':
    main()
