#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import argparse
import sys

# Third-part library import.

# Project library import.
import Read_histo
import Show_datas

######################

def opt_arg():
    """
    Option and arguments parse.
    @parameters : none.
    @return : parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Formated display the apt history file.",
                                     argument_default="raw")

    parser.add_argument("-r","--raw",
                        action="store_true",
                        default=True,
                        help="Display with raw format as though using 'cat' command (default option)")

    parser.add_argument("-n","--niceraw",
                        action="store_true",
                        default=False,
                        help="Display with raw format,but with a littel formatting")

    parser.add_argument("-d","--date",
                        type=str,
                        default=None,
                        help="Display for a date, or since this date (also use -u option)")

    parser.add_argument("-u","--until",
                        type=str,
                        default=None,
                        help="Display until this date (also use -d option)")

    parser.add_argument("--showdates",
                        action="store_true",
                        default=False,
                        help="Show dates which are be able only")

    return parser.parse_args()

def main():
    """
    Main function.
    @parameters : none.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    print("")
    args = opt_arg()

    show_datas = Show_datas.Show_datas()

    if args.niceraw:
        show_datas.nice_raw()

    elif args.showdates:
        # TODO: will be implementing.
        print("Not yet implemented !")
        args.raw = False

    elif args.date:
        args.raw = False
        try:
            show_datas.date = args.date
            show_datas.nice_raw_date()
        except SyntaxError as e:
            print(e, "\n")

    elif args.until:
        print("Date =", args.date)
        print("Until =", args.until)
        # TODO: will be implementing.
        args.raw = False
        show_datas.date = args.date
        show_datas.end_date = args.until
        print("Will be implementing")

    elif args.raw:
        show_datas.raw()

    return 0

######################

if __name__ == "__main__":
    rc = main()
    sys.exit(rc)

