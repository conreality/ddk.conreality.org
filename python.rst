*************************
Conreality DDK for Python
*************************

**(To be written.)**

Installation
============

The DDK requires the following prerequisites on the system:

* Python (3.4+)
* Lupa (1.2+)
* NumPy (1.10.4+)
* OpenCV (3.0+) with Python 3.x bindings

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

**(To be written.)**

.. py:module:: conreality.ddk.driver

Module ``conreality.ddk.driver``
--------------------------------

**(To be written.)**

.. py:class:: Logger()

.. py:method:: Logger.open(verbosity=syslog.LOG_NOTICE)

.. py:method:: Logger.close()

.. py:method:: Logger.loop()

.. py:method:: Logger.log(priority, message, *args)

   Logs a message to the system log (typically, :file:`/var/log/syslog`).

   :rtype: None

.. py:method:: Logger.panic(message, *args)

   ``LOG_EMERG``

.. py:method:: Logger.alert(message, *args)

   ``LOG_ALERT``

.. py:method:: Logger.critical(message, *args)

   ``LOG_CRIT``

.. py:method:: Logger.error(message, *args)

   ``LOG_ERR``

.. py:method:: Logger.warning(message, *args)

   ``LOG_WARNING``

.. py:method:: Logger.notice(message, *args)

   ``LOG_NOTICE``

.. py:method:: Logger.info(message, *args)

   ``LOG_INFO``

.. py:method:: Logger.debug(message, *args)

   ``LOG_DEBUG``

.. py:class:: Driver(argv=sys.argv, argparser=ArgumentParser, input=sys.stdin, output=sys.stdout)

.. py:method:: Driver.init()

   Executed on initialization of the driver process.

.. py:method:: Driver.exit()

   Executed on termination of the driver process.

.. py:method:: Driver.loop()

   Executed on each tick of the driver event loop.

.. py:method:: Driver.stop()

   Stops the driver event loop, terminating the driver process.

.. py:class:: ArgumentParser()

.. py:class:: DataDirectory(*path)

.. py:exception:: DataDirectoryException(error)

.. py:exception:: SignalException(signum)

.. py:module:: conreality.ddk.sysexits

Module ``conreality.ddk.sysexits``
----------------------------------

**(To be written.)**

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
