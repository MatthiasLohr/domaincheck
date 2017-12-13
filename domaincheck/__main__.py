
import argparse
from domaincheck import check
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', nargs='*', help='File with domain names, one domain per line')
    parser.add_argument('domain', nargs='*', help='Domain name to check')
    args = parser.parse_args()

    if args.input_file:
        for filename in args.input_file:
            with open(filename) as stream:
                for domain in stream.readlines():
                    check(domain)

    for domain in args.domain:
        check(domain)


if __name__ == '__main__':
    sys.exit(main())
