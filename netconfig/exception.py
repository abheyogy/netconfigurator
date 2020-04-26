'''Custom exception class for NetConfigurator program.'''


class NetConfiguratorError(Exception):
    '''NetConfiguratorError customized exception.'''

    def __init__(self, *args):
        '''Initialize this custom exception type to wrap around the Exception
        message.'''

        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        '''Exception error message wrapper.'''

        if self.message:
            return 'NetConfiguratorError, {0} '.format(self.message)
        else:
            return 'NetConfiguratorError:'


class TemplatorError(NetConfiguratorError):
    '''TemplateError customized exception to raise errors specific to populating
    variables in template configuration files.'''

    pass


class ConfiguratorError(NetConfiguratorError):
    '''ConfiguratorError customized exception to raise errors specific to
    loading configuration variables.'''
