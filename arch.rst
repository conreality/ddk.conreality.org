*********************
Software Architecture
*********************

This chapter explains where Conreality device drivers fit in with the rest
of the system and application layers.

Process Model
=============

**(To be written.)**

Execution Environment
=====================

Device drivers are executed by and as subprocesses of the Conreality daemon
(``conreald``), which provides the following execution environment for the
driver process:

* The process has three pre-opened file descriptors (0, 1, and 2), for the
  standard input, output, and error streams.

* The process's user and group privileges are adjusted (depending on
  configuration).

* The process's scheduling policy and priority are adjusted (depending on
  configuration).

* The process's CPU affinity mask is set so as to pin it to specific CPU
  cores (depending on configuration).

When executing drivers manually as standalone processes--in particular,
during driver development--it may be necessary to emulate some aspects of
this execution environment by using utilities such as :manpage:`su(1)`,
:manpage:`chrt(1)`, :manpage:`taskset(1)`, and :manpage:`nice(1)` when
executing the standalone driver process.

Process Privileges
------------------

**(To be written.)**

Process Scheduling
------------------

**(To be written.)**

Signal Handling
---------------

It is the responsibility of the driver process to set up signal handlers and
correctly handle signals delivered by the kernel. The following
signal-handling behaviors are normative for driver processes:

* ``SIGHUP``: reload configuration.

* ``SIGINT``: exit the process.

* ``SIGPIPE``: exit the process.

* ``SIGTERM``: exit the process.

Command-Line Arguments
----------------------

Even though driver binaries are not intended to be directly executed by end
users, they should nonetheless implement standard command-line argument
processing so as to handle at least the following common options:

* ``-h``, ``--help``: show a help message and exit

* ``-q``, ``--quiet``: suppress superfluous output

* ``-v``, ``--verbose``: increase the verbosity level (could be given multiple times)

* ``-d``, ``--debug``: enable debugging output

Driver binaries may accept additional positional and/or optional arguments,
but must be able to execute using sane defaults when none are given.

Error Logging
-------------

Drivers must log any warnings and errors to the system log using
:manpage:`syslog(3)` interfaces. They may also log additional informational
messages and notices to the system log, using the appropriate lower priority
levels.

Logging should be configured with the program identification ``"conreality"``,
the option flags ``LOG_PID | LOG_CONS | LOG_NDELAY``, and the facility
``LOG_DAEMON``.

The log mask shall be set as follows:

* Default: ``LOG_NOTICE``

* ``-q``, ``--quiet``: ``LOG_WARNING``

* ``-v``, ``--verbose``: ``LOG_INFO``

* ``-d``, ``--debug``: ``LOG_DEBUG``

Exit Codes
----------

Driver processes must terminate using standard :manpage:`sysexits(3)` exit
codes, as per the following guidelines:

+------+--------------------+--------------------------------------------------+
| Code | Label              | Summary                                          |
+======+====================+==================================================+
|    0 | ``EX_OK``          | successful termination                           |
+------+--------------------+--------------------------------------------------+
|   64 | ``EX_USAGE``       | command line usage error                         |
+------+--------------------+--------------------------------------------------+
|   65 | ``EX_DATAERR``     | data format error                                |
+------+--------------------+--------------------------------------------------+
|   66 | ``EX_NOINPUT``     | cannot open input                                |
+------+--------------------+--------------------------------------------------+
|   67 | ``EX_NOUSER``      | addressee unknown                                |
+------+--------------------+--------------------------------------------------+
|   68 | ``EX_NOHOST``      | host name unknown                                |
+------+--------------------+--------------------------------------------------+
|   69 | ``EX_UNAVAILABLE`` | service unavailable                              |
+------+--------------------+--------------------------------------------------+
|   70 | ``EX_SOFTWARE``    | internal software error                          |
+------+--------------------+--------------------------------------------------+
|   71 | ``EX_OSERR``       | system error (e.g., can't fork)                  |
+------+--------------------+--------------------------------------------------+
|   72 | ``EX_OSFILE``      | critical OS file missing                         |
+------+--------------------+--------------------------------------------------+
|   73 | ``EX_CANTCREAT``   | can't create (user) output file                  |
+------+--------------------+--------------------------------------------------+
|   74 | ``EX_IOERR``       | input/output error                               |
+------+--------------------+--------------------------------------------------+
|   75 | ``EX_TEMPFAIL``    | temp failure; user is invited to retry           |
+------+--------------------+--------------------------------------------------+
|   76 | ``EX_PROTOCOL``    | remote error in protocol                         |
+------+--------------------+--------------------------------------------------+
|   77 | ``EX_NOPERM``      | permission denied                                |
+------+--------------------+--------------------------------------------------+
|   78 | ``EX_CONFIG``      | configuration error                              |
+------+--------------------+--------------------------------------------------+
