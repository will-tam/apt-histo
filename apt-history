#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.

######################

APTHISTOFILE = "/var/log/apt/history.log"

######################

def reform_apt_histofile(histofile):
    """
    Reform all apt history file into list of action.
    @parameters : histofile = the whole path of apt history file.
    @return : yield a bloc of apt history as list.
    """
    with open(histofile, "rt") as histof:
        for line in histof:
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

def prepare_sub_cde(subcommands):
    """
    Generator to prepare sub commands to be beautifully displayed (huhu).
    @parameters : subcommands = apt sub-commands to dispaly with packages worked on.
    @return : the sub command and their packages.
    """
    subcdes = sorted(subcommands.keys())
    for subcde in subcdes:
        yield [subcde.strip(), subcommands[subcde].strip()]

def prepare_pkg(packages):
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

def beautify(bloc):
    """
    Display bloc as better way.
    @parameters : bloc = the bloc of datas to display
    @return : none.
    """
    start_date = bloc["Start-Date"].strip().split("  ")
    end_date = bloc["End-Date"].strip().split("  ")
    used_apt_cde = bloc["Commandline"].strip()
    what_done = bloc["SubCommands"]
    print("Start in {}, at {}".format(start_date[0], start_date[1]))
    print("End in {}, at {}".format(end_date[0], end_date[1]))
    print("  Done with {}".format(used_apt_cde))
    for subcde in prepare_sub_cde(what_done):
        print("    {} :".format(subcde[0]))
        for pkg in prepare_pkg(subcde[1]):
            # TODO : display according option line.
#            print("\t    {}".format(pkg[0]))
            print("{} ".format(pkg[0]), end="")
        print("")

def main(arg):
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    for bloc in reform_apt_histofile(APTHISTOFILE):
        beautify(bloc)

        print("")

    return 0

######################

if __name__ == "__main__":
    rc = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(rc)

