
import argparse
import logging
import sys

from domaincheck import check
from domaincheck import CheckResult


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', nargs='*', help='File with domain names, one domain per line')
    parser.add_argument('domain', nargs='*', help='Domain name to check')
    parser.add_argument('--hide-used', action='store_true')
    parser.add_argument('--hide-for-sale', action='store_true')
    args = parser.parse_args()

    results = []
    found_error = False

    if args.input_file:
        for filename in args.input_file:
            with open(filename) as stream:
                for domain in stream.readlines():
                    result = check(domain)
                    results.append((domain, result))

    for domain in args.domain:
        result = check(domain)
        results.append((domain, result))

    for domain, result in results:
        if result == CheckResult.INVALID:
            logging.error('{} is invalid'.format(domain))
            found_error = True
        elif result == CheckResult.USED and not args.hide_used:
            logging.info('{} is used'.format(domain))
        elif result == CheckResult.FOR_SALE and not args.hide_for_sale:
            logging.info('{} is available for sale'.format(domain))
        elif result == CheckResult.AVAILABLE:
            logging.info('{} is available for registration'.format(domain))

    return 1 if found_error else 0


if __name__ == '__main__':
    sys.exit(main())
