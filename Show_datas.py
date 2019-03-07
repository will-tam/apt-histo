# -*- coding: utf-8 -*-

# Standard libraries import.
import re

# Third libraries import.


# Projet modules import.
import Read_histo

######################

class Show_datas(Read_histo.Read_histo):
    """
    Show datas as will.

    Public attributes.
        datas = datas read.
    """

    # Private attributes.
        # __date = date, or begin date to see.
        # __end_date = end date to see.


    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        self.__date = None
        self.__end_date = None
        self.datas = None

        super().__init__()

#        print(self.histo_files)

    @property
    def date(self):
        """
        Not used.
        """
        pass

    @date.setter
    def date(self, date):
        """
        @parameters : date = date, or begin date to see.
        @return : none.
        """
        # TODO: check date's format.
        if self.__check_date(date):
            self.__date = date
        else:
            raise SyntaxError("Format of date miss understanding")

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
        for histo_file in self.histo_files:
            print("In {} :".format(histo_file))
            for bloc in self.__reform_apt_histofile(histo_file):
                start_date = bloc["Start-Date"].strip().split("  ")
                end_date = bloc["End-Date"].strip().split("  ")
                used_apt_cde = bloc["Commandline"].strip()
                what_done = bloc["SubCommands"]
                print(" Start in {}, at {}".format(start_date[0], start_date[1]))
                print(" End in {}, at {}".format(end_date[0], end_date[1]))
                print("   Done with {}".format(used_apt_cde))
                for subcde in self.__prepare_sub_cde(what_done):
                    print("     {} :".format(subcde[0]))
                    print("       ", end='')
                    for pkg in self.__prepare_pkg(subcde[1]):
                        print("{} ".format(pkg[0]), end="")

                print("\n")
            print("\n")


    # Private methods.
    def __check_date(self, date):
        """
        Check the given date.setter
        @parameters : date = date to check format.
        @return : True if date format is ok, everelse False.
        """
        date_ok = re.split('(\d{4})(-)(\d{2})(-)(\d{2})', "-", date)
        print(date_ok)
        return True

    def __prepare_pkg(self, packages):
        """
        Prepare the packages to be displayed as we wish.
        @parameters : pkgs = packages to prepare to be displayed.
        @return : list of packages.
        """
        pkgs = []
        for pkg in packages.split("),"):
            # TODO : find something better. Uggly !!!!!! (Try re module).
            np = pkg.split(":")[0].strip()
            arch = pkg.split(":")[1].split(" (")[0]
            vers = pkg.split(":")[1].split(" (")[1].split(", ")[0]
            # TODO : try if something other
    #        other = pkg.split(":")[1].split(" (")[1].split(", ")[1]

            pkgs.append([np, arch, vers, ])

        return pkgs

    def __prepare_sub_cde(self, subcommands):
        """
        Generator to prepare sub commands to be beautifully displayed (huhu).
        @parameters : subcommands = apt sub-commands to dispaly with packages worked on.
        @return : the sub command and their packages.
        """
        subcdes = sorted(subcommands.keys())
        for subcde in subcdes:
            yield [subcde.strip(), subcommands[subcde].strip()]

    def __reform_apt_histofile(self, histofile):
        """
        Reform all apt history file into list of action.
        @parameters : histofile = the whole path of apt history file.
        @return : yield a bloc of apt history as list.
        """
        for line in self.read_for(histofile):
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
            else:
                line = "You should not see me !"

######################

if __name__ == "__main__":
    help(My_class)
