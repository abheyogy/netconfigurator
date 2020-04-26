"""Program to fetch data from a configuration file."""
import yaml


class ConfigFile():
    """Fetch data from a configuration file. Based on the configuration, decide which format to use, YAML or JSON."""

    def __init__(self, conf_file):
        '''Load variables from configuration file.'''

        with open(conf_file, 'r') as cnf_file:
            self.conf = yaml.safe_load(cnf_file)

    def fetch_values(self):
        '''Fetch configuration values.'''

        return self.conf
