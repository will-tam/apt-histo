# -*- coding: utf-8 -*-

# Standard libraries import.


# Third libraries import.


# Projet modules import.
import Read_histo

######################

class Show_datas(Read_histo.Read_histo):
    """
    Show datas as will.

    Public attributes.
        date = date, or begin date to see.
        end_date = end date to see.
        datas = datas read.
    """

    # Private attributes.


    # Public methods.

    def __init__(self, date=None, end_date=None):
        """
        __init__ : initiate class
        @parameters : date = date, or begin date to see.
                      end_date = end date to see.
        @return : none.
        """
        self.date = date
        self.end_date = end_date
        self.datas = None

        super().__init__()

#        print(self.histo_files)

    def raw(self):
        """
        Reading (un)compressed history file, and print as-is each line on terminal.
        @parameters : none.
        @return : none.
        """
        for file in self.histo_files:
            print("{} {}".format(4*"-", file))
            for data in self.read_for(file):
                print(data, end='')

            print("")

    def nice_raw(self):
        """
        Reading (un)compressed history file, and print each line on terminal within better way.
        @parameters : none.
        @return : none.
        """
        for file in self.histo_files:
            for data in self.read_for(file):
#                print(data, end='')
                for bloc in self.__reform_apt_histofile(APTHISTOFILE):
                    pass
#        for bloc in self.__reform_apt_histofile(APTHISTOFILE):
#            start_date = bloc["Start-Date"].strip().split("  ")
#            end_date = bloc["End-Date"].strip().split("  ")
#            used_apt_cde = bloc["Commandline"].strip()
#            what_done = bloc["SubCommands"]
#            print("Start in {}, at {}".format(start_date[0], start_date[1]))
#            print("End in {}, at {}".format(end_date[0], end_date[1]))
#            print("  Done with {}".format(used_apt_cde))
#            for subcde in prepare_sub_cde(what_done):
#                print("    {} :".format(subcde[0]))
#                for pkg in prepare_pkg(subcde[1]):
#                    # TODO : display according option line.
#        #            print("\t    {}".format(pkg[0]))
#                    print("{} ".format(pkg[0]), end="")
#
#                print("")


    # Private methods.

    def __reform_apt_histofile(histofile):
        """
        Reform all apt history file into list of action.
        @parameters : histofile = the whole path of apt history file.
        @return : yield a bloc of apt history as list.
        """
        for file in self.histo_files:
            line = line.strip()
            if line:
                key = line.split(":", 1)[0]
                value = line.split(":", 1)[1]
                if line.find("Start-Date") > -1:
                    bloc = {"SubCommands" : {}}
                    bloc[key] = value
                elif line.find("End-Date") > -1:
                    bloc[key] = value
                    yield bloc
                elif line.find("Commandline") > -1:
                    bloc[key] = value
                else:
                    subcde = line.strip().split(":", 1)[0]
                    pkg = line.strip().split(":", 1)[1]
                    bloc["SubCommands"][subcde] = pkg

######################

if __name__ == "__main__":
    help(My_class)
