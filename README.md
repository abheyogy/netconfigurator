Netconfigurator
---------------


Netconfigurator is a tool which can either be run as a service or invoked dynamically as a terminal program via. the Command line interface.

Primarily, this service shall/will create a Nginx configuration file. This Nginx configuration file is created from a templated Nginx configuration file. The infromation to fill in the blanks (templated variables) is expected to be given to this program as an input YAML file.

Although, initially designed specifically with Nginx configurations in mind, this program could potentially also work for any other programs configuration files which minimal changes to this program.

Roadmap
-------

- Add support for other message queues like Qpid, RabbitMQ, etc.
- Add support for other services.
- Extend test cases.

Contributors
------------

If you wish to be a part of this project, feel free to open up a Pull Request, or report an issue, feature requests ... 

Author: Pranav Salunke <abheyogy@gmail.com>
List of contributors:
  - Hacker_A
  - Hacker_B
