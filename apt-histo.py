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

def main(arg):
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    show_datas = Show_datas.Show_datas()

#    show_datas.raw()

    show_datas.nice_raw()

    return 0

######################

if __name__ == "__main__":
    rc = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(rc)

