Netconfigurator
===============


Netconfigurator is a tool which can either be run as a service or invoked dynamically as a terminal program via. the Command line interface.

Primarily, this service shall/will create a Nginx configuration file. This Nginx configuration file is created from a templated Nginx configuration file. The infromation to fill in the blanks (templated variables) is expected to be given to this program as an input YAML file.

Although, initially designed specifically with Nginx configurations in mind, this program could potentially also work for any other programs configuration files which minimal changes to this program.


Architecture
------------

- Command Line interface and if it makes sense, an API in future.
- A module to fetch configuration files & variables.
- A module to populate configuration variables to configuration files.
- Customized exceptions.
- Logger for logging & log levels.


```
+--------------+   +----------------------------------------+
|              |   |                                        |
|  CLI / API   +--->    Manager/Engine Class                |
|              |   |                                        |
+--------------+   |    Stitches modules/classes togather.  |
                   |                                        |
          +--------+------+---------------------------------+
          |               |
+---------v----+    +-----v-------+   +---------------------+
|              |    |             |   | Custom Exceptions   |
| Fetch Conf   |    |  Populate   |   |        Class        |
|              |    | Config File |   |                     |
| - YAML       |    |             |   |                     |
| | Streams    |    | - Nginx     |   +---------------------+
| | Buffers    |    | - Other ... |   +---------------------+
| - DB/Cache   |    |             |   |                     |
|              |    |             |   |  Logger             |
|              |    |             |   |                     |
|              |    |             |   |                     |
+--------------+    +-------------+   +---------------------+
```

Try me out!
-----------

If you wish to give this tool a try, please get your hands dirty ...

* You need Python 3.6 or above for this program to work. It may work with
  older Python3 versions but I did not test it or plan to support it.
* I am using PyEnv, or even plain old VirtualEnv shall suffice.
* Please install the required packages as per the given command below:
  ```
    $ pip install -r requirements.txt
  ```
* Then cd into the netconfig folder to run the program:
  ```
    $ python netconfig.py
  ```
* Please make sure that you have either modified the path to the configuration
  file `input.yaml` in the netconfig.py file or have updated the same in the etc
  folder.
* By default it tries to look for `input.yaml` & `nginx.conf.j2` at the `etc` folder
  located at the root of this repository. The `nginx.conf.j2` file has been provided
  unless you have some major changes in there, it should suffice for most ...
  if not all.


Roadmap
-------

- Create appropriate documentation.
- Add appropriate log levels and improve on overall logging.
- Update the custom exceptions for better error handling.
- Add support for other message queues like Qpid, RabbitMQ, etc.
- Add support for other services.
- Extend test cases.


Contributors
------------

If you wish to be a part of this project, feel free to open up a Pull Request, or report an issue, feature requests ...

Author: Pranav Salunke <abheyogy@gmail.com>
List of contributors:
  - Pranav Salunke <abheyogy@gmail.com>
