#!/usr/bin/env python3
"""Program to fetch configuration data from a YAML file and populate template variables to
dynamically generate Nginx configuration file for various Nginx related configurations.

This is the manager/engine program which delegates and ties in togather functionality from
various modules/programs for abstracting away unnecessary complixity following OOPS paradigm
and other related Computer design patterns.
"""

import configurator.configurator as configurator
from templator import Templator
from exception import *


def main(config, tmpl_folder):
    '''Main program.'''

    try:
        cnf = configurator.Configurator(config_file=config)
        cnf_vars = cnf.get_conf_vars()
        tmpl = Templator(config_vars=cnf_vars, tmpl_folder=tmpl_folder)
        tmpl.create_conf()
    except ConfiguratorError as ex_cnf:
        print("Seems like a configuration error:\n", ex_cnf)
    except TemplatorError as ex_tmpl:
        print("Seems like a template error:\n", ex_tmpl)
    except NetConfiguratorError as ex_netcnf:
        print("Seems like a NetConfigurator error:\n", ex_netcnf)


if __name__ == "__main__":
    '''If invoked as a main program.'''

    main("../etc/input.yaml", "../etc/")
