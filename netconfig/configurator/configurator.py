"""Configurator is responsible to carry out the task of populating the
datastructure from given set of input variables and return them to the
original caller of this module.
"""

from exception import *


class Configurator():
    """Configurator generates the datastructure which contains various
    variables required. The actual extraction of the variables is delegated
    to the class responsible to extract data from either a message queue or a
    YAML file. This program will make a decision based on its configuration or
    CLI option to either fetch the variables from a message queue or from a
    configuration file."""

    def __init__(self, config_file=None, queue_topic=None):
        '''Configurator constructor to load require configuration file.'''

        if config_file:
            self.fetch_values(config_file)
        elif queue_topic:
            self.queues()
        else:
            raise exception.ConfiguratorError('No configuration file source \
                    provided, please provide a valid configuration source')

    def fetch_values(self, config_file):
        '''This method loads configuration variables from configuration files
        by calling the config_file python program and loading the required
        configuration files.'''

        #TODO(pranav): Please improve dynamic module loading logic.
        # May be a helper function?
        import configurator.load_configfile as load_config

        self.config_vars = None

        try:
            cnf = load_config.ConfigFile(config_file)
            self.config_vars = cnf.fetch_values()
        except TypeError as ex:
            raise exception.ConfigurationError("Error while attempting to \
                    read configuration file:", ex)
        except config_file.yaml.YAMLError as ex:
            raise exception.ConfigurationError("Error while attempting to \
                    load configuration file:", ex)

    def get_conf_vars(self):
        '''Get configuration values in form of a dict datastructure.'''

        return self.config_vars

    def queues(self):
        '''This method loads configuration variables from a message queue
        or a buffer stream.'''

        raise NotImplementedError("Queues are not implemented yet!")
