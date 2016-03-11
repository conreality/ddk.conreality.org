*************************
Conreality DDK for Python
*************************

**(To be written.)**

The Python ecosystem affords drivers access to much great software such
as, to name just a few examples: `ROS`_, `OpenCV`_, `scikit-image`_,
`scikit-learn`_, `TensorFlow`_, `NuPIC`_, `NLTK`_, and `spaCy`_.  Further,
with the language being one of the established *lingua francas* of modern
programming, the Python DDK enables the largest possible audience to
contribute to the development of Conreality drivers.

.. _ROS:          http://www.ros.org/
.. _OpenCV:       http://opencv.org/
.. _scikit-image: http://scikit-image.org/
.. _scikit-learn: http://scikit-learn.org/
.. _TensorFlow:   https://www.tensorflow.org/
.. _NLTK:         http://www.nltk.org/
.. _NuPIC:        http://numenta.org/
.. _spaCy:        https://spacy.io/

Installation
============

The DDK requires the following prerequisites on the system:

* `Python`_ (3.4+)
* `Lupa`_ (1.2+)
* `NumPy`_ (1.10.4+)
* `OpenCV`_ (3.0+) with `Python 3.x bindings <OpenCV/Py_>`_

.. _Python:       https://www.python.org/
.. _Lupa:         https://pypi.python.org/pypi/lupa
.. _NumPy:        https://pypi.python.org/pypi/numpy
.. _OpenCV/Py:    http://docs.opencv.org/master/d6/d00/tutorial_py_root.html

Tutorial
========

**(To be written.)**

.. code-block:: python

   from conreality import ddk

Defining the Driver Event Loop
------------------------------

**(To be written.)**

.. literalinclude:: python/my_driver.py
   :pyobject: MyDriver

Parsing Command-Line Arguments
------------------------------

**(To be written.)**

.. literalinclude:: python/my_driver.py
   :pyobject: MyArgumentParser

.. code-block:: python

   if __name__ == '__main__':
     import sys
     with MyDriver(argparser=MyArgumentParser) as driver:
       sys.exit(driver.run())

Reference
=========

**(To be written.)**

.. py:module:: conreality.ddk

.. py:module:: conreality.ddk.camera

Module ``conreality.ddk.camera``
--------------------------------

This module contains support code for generic camera APIs.

.. py:class:: CameraRegistry()

.. py:class:: CameraDirectory(id)

.. py:class:: CameraFeed(dir)

.. py:module:: conreality.ddk.driver

Module ``conreality.ddk.driver``
--------------------------------

This module contains support code for implementing driver programs.

.. py:class:: Logger()

   Mixin that implements logging to the system log.

.. py:method:: Logger.open(verbosity=syslog.LOG_NOTICE)

   Opens the connection to the system log.

.. py:method:: Logger.close()

   Closes the connection to the system log.

.. py:method:: Logger.log(priority, message, *args)

   Logs a message to the system log (typically, :file:`/var/log/syslog`).

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.panic(message, *args)

   Logs a message to the system log with ``LOG_EMERG`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.alert(message, *args)

   Logs a message to the system log with ``LOG_ALERT`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.critical(message, *args)

   Logs a message to the system log with ``LOG_CRIT`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.error(message, *args)

   Logs a message to the system log with ``LOG_ERR`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.warning(message, *args)

   Logs a message to the system log with ``LOG_WARNING`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.notice(message, *args)

   Logs a message to the system log with ``LOG_NOTICE`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.info(message, *args)

   Logs a message to the system log with ``LOG_INFO`` priority.

   :return: ``self``
   :rtype: Logger

.. py:method:: Logger.debug(message, *args)

   Logs a message to the system log with ``LOG_DEBUG`` priority.

   :return: ``self``
   :rtype: Logger

.. py:class:: Driver(argv=sys.argv, argparser=ArgumentParser, input=sys.stdin, output=sys.stdout)

.. py:method:: Driver.init()

   Executed on initialization of the driver process.
   Override this in your subclass.

.. py:method:: Driver.exit()

   Executed on termination of the driver process.
   Override this in your subclass.

.. py:method:: Driver.loop()

   Executed on each tick of the driver event loop.
   Override this in your subclass.

.. py:method:: Driver.stop()

   Stops the driver event loop, terminating the driver process.

.. py:class:: ArgumentParser()

   The default implementation of command-line argument parsing.

.. py:class:: DataDirectory(*path)

.. py:exception:: DataDirectoryException(error)

.. py:module:: conreality.ddk.sysexits

Module ``conreality.ddk.sysexits``
----------------------------------

This module contains constants for the standard exit codes that driver
programs should use to indicate their termination status.

.. py:data:: EX_OK          = 0  # successful termination
.. py:data:: EX_USAGE       = 64 # command line usage error
.. py:data:: EX_DATAERR     = 65 # data format error
.. py:data:: EX_NOINPUT     = 66 # cannot open input
.. py:data:: EX_NOUSER      = 67 # addressee unknown
.. py:data:: EX_NOHOST      = 68 # host name unknown
.. py:data:: EX_UNAVAILABLE = 69 # service unavailable
.. py:data:: EX_SOFTWARE    = 70 # internal software error
.. py:data:: EX_OSERR       = 71 # system error (e.g., can't fork)
.. py:data:: EX_OSFILE      = 72 # critical OS file missing
.. py:data:: EX_CANTCREAT   = 73 # can't create (user) output file
.. py:data:: EX_IOERR       = 74 # input/output error
.. py:data:: EX_TEMPFAIL    = 75 # temp failure; user is invited to retry
.. py:data:: EX_PROTOCOL    = 76 # remote error in protocol
.. py:data:: EX_NOPERM      = 77 # permission denied
.. py:data:: EX_CONFIG      = 78 # configuration error
