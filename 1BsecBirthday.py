#Your 1Bsec Birthday!
#adapted to python3 from https://gist.githubusercontent.com/Westacular/5996271/raw/147384089e72f4009f177cd2d5c089bb2d8e5934/birthday_second_counter.py

# -*- coding: utf-8 -*-

import sys
import argparse
import traceback

import dateutil.parser
import dateutil.tz
from datetime import datetime, timedelta
import time


def parse_my_args(arguments=None):
    parser = argparse.ArgumentParser(
        description='Uses the given birthdate (+ time) to calculate when you will reach the milestone age '
                    'in seconds, and then displays a countdown timer.')
    parser.add_argument(
        'birthdate', metavar='BIRTHDATE', type=dateutil.parser.parse,
        help='Date and time of birth, ideally with time zone specified, e.g., "1981-11-04 14:50:00-05:00"')
    parser.add_argument(
        'milestone', metavar='MILESTONE', type=int, nargs='?', default=1e9,
        help='The milestone age in seconds (Default: one billion seconds)')

    if arguments is not None:
        if isinstance(arguments, list):
            args = parser.parse_args(arguments)
        elif isinstance(arguments, str):
            args = parser.parse_args(arguments.split())
        else:
            raise TypeError("'arguments' must be either a string or a list of strings")
    else:
        args = parser.parse_args()

    return args


def main(arguments=None):
    args = parse_my_args(arguments)

    bday = args.birthdate
    if bday.tzinfo is None:
        print("Assuming local time zone for birthday.")
        bday = bday.replace(tzinfo=dateutil.tz.tzlocal())
        bday_utc = bday.astimezone(dateutil.tz.gettz('UTC'))

    print("Birthday is", bday)

    target_utc = bday_utc + timedelta(seconds=args.milestone)
    target_local = target_utc.astimezone(dateutil.tz.tzlocal())

    sys.stdout.write("{milestone:.0f} seconds of age will occur at {target}\n\n".format(
        milestone=args.milestone, target=target_local))

    sys.stdout.write("UNIX timestamps: Birthday: {birthday}    Milestone: {target}\n\n".format(
        birthday=(bday_utc - datetime(1970,1,1, tzinfo=dateutil.tz.gettz('UTC'))).total_seconds(),
        target=(target_utc - datetime(1970,1,1, tzinfo=dateutil.tz.gettz('UTC'))).total_seconds()))

    while True:
        now = datetime.utcnow().replace(tzinfo=dateutil.tz.gettz('UTC'))
        sys.stdout.write("\r{0:12.1f}\t{1:12.1f}".format((now - bday_utc).total_seconds(), (target_utc - now).total_seconds()))
        sys.stdout.flush()
        time.sleep(0.1)



if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:
        sys.stdout.write("\n")
        sys.exit(0)
    except SystemExit as e:
        raise e
    except argparse.ArgumentError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
        traceback.print(exc())
        sys.exit(1)
/
