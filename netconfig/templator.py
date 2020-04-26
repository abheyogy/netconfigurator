"""Templator generates Nginx configuration files."""

from jinja2 import Environment, FileSystemLoader
import os

from exception import *


class Templator():
    """Templator takes in the configuration data in a data structure format and
    generates the appropriate Nginx configuration files which is rather taking
    the nginx template file and populating the jinja templated variables to
    generate a final nginx file."""

    def __init__(self, config_vars=None, tmpl_folder=None):
        '''Instantiates Templator class.'''

        if config_vars:
            self.config_vars = config_vars
        else:
            raise TemplatorError("Configuration Variables not found.\
                    I'm a computer program, not a magician!!!")

        if tmpl_folder:
            self.tmpl_folder = tmpl_folder
            print("Rendering Jinja file ...")
        else:
            raise TemplatorError("Template File not found.\
                    Seriously, computers cannot do no magik!!!\
                    We barely even have any intelligence of our own.")

    def create_conf(self, write_to='/tmp/nginx.conf'):
        '''Create configuration file based on the template and input
        variables.'''



        env = Environment(
                loader=FileSystemLoader(os.path.abspath(self.tmpl_folder)),
                )
        env.trim_blocks = True
        env.lstrip_blocks = True
        env.rstrip_blocks = True

        template = env.get_template('nginx.conf.j2')
        output = template.render(self.config_vars)
        with open(write_to, 'w') as nginx_conf:
            nginx_conf.write(output)

        import pprint
        pprint.pprint(output)
