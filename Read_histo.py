# -*- coding: utf-8 -*-

# Standard libraries import.
import glob
import gzip
import re
#import collections

# Third libraries import.


# Projet modules import.


######################

class Read_histo():
    """
    Read in APTHISTOFILE the history.log[.*.gz] files and keep it
    in some dictionnary.

    Public attributes.
        histo_files = list of history files in APTHISTOFILE.
    """

    APTHISTOFILE = "/var/log/apt/history.log*"  # Don't care about os.pathsep, here we speak about Debian like distro.

    # Private attributes.
        # __start_date = compiled regex to search dates.

    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none
        @return : none.
        """
        self.histo_files = self.__spec_sort(glob.glob(Read_histo.APTHISTOFILE))

    def read_for(self, file):
        """
        Read the apt history files as will.
        @parameters : func = function using opened file descritor.
        @return : none.
        """
        if file.rfind(".gz") > -1:
            with gzip.open(file, 'rt') as fd:
                for data in fd:
                    yield data
                fd.close()
        else:
            with open(file, 'rt') as fd:
                for data in fd:
                    yield data
                fd.close()

    # Private methods.
    def __spec_sort(self, datas):
        """
        Special sort of files with numbers in name.
        Invent again the wheel, cause the sorted() doens't sort as i wish it.
        @parameters : datas = list of what to sort.
        @return : sorted list.
        """
        datas_sorted = []

        two_digit = re.compile("\.(\d{2})\.")       # Looking for xxx.log.nn.
        one_digit = re.compile("\.(\d{1})\.")       # Looking for xxx.log.n.

        d2 = sorted([data for data in datas if two_digit.search(data)], reverse=True)
        d1 = sorted([data for data in datas if one_digit.search(data)], reverse=True)

        datas_sorted.extend(d2)
        datas_sorted.extend(d1)
        datas_sorted.append(Read_histo.APTHISTOFILE[:-1])

        return datas_sorted

#    def __fill_apt_histo(self, fdc):
#        """
#        Read (un)compressed history file, and return dates found in it
#        @parameters : fdc = the file descriptor common.
#        @return : found dates list.
#        """
#        dates = []
#
##        self.__start_date
#        for line in fdc:
#            result = self.__start_date.match(line)
#            if result:
#                print(result.groups())
#
#        return dates


######################

if __name__ == "__main__":
    help(My_class)
