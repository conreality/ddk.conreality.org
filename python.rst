*************************
Conreality DDK for Python
*************************

Tutorial
========

.. code-block:: python

   from conreality import ddk

Defining the Driver Event Loop
------------------------------

.. literalinclude:: python/my_driver.py
   :pyobject: MyDriver

Parsing Command-Line Arguments
------------------------------

.. literalinclude:: python/my_driver.py
   :pyobject: MyArgumentParser

.. code-block:: python

   if __name__ == '__main__':
     MyDriver(argparser=MyArgumentParser).run()

Reference
=========

.. py:module:: conreality.ddk

.. py:module:: conreality.ddk.camera

Module ``conreality.ddk.camera``
--------------------------------

.. py:module:: conreality.ddk.driver

Module ``conreality.ddk.driver``
--------------------------------

.. py:class:: Driver(argv=sys.argv, argparser=ArgumentParser)

.. py:method:: Driver.init()

.. py:method:: Driver.exit()

.. py:method:: Driver.loop()

.. py:method:: Driver.log(priority, message, *args)

  :rtype: None

.. py:method:: Driver.panic(message, *args)

   ``LOG_EMERG``

.. py:method:: Driver.alert(message, *args)

   ``LOG_ALERT``

.. py:method:: Driver.critical(message, *args)

   ``LOG_CRIT``

.. py:method:: Driver.error(message, *args)

   ``LOG_ERR``

.. py:method:: Driver.warning(message, *args)

   ``LOG_WARNING``

.. py:method:: Driver.notice(message, *args)

   ``LOG_NOTICE``

.. py:method:: Driver.info(message, *args)

   ``LOG_INFO``

.. py:method:: Driver.debug(message, *args)

   ``LOG_DEBUG``

.. py:class:: ArgumentParser()

.. py:class:: DataDirectory(*path)

.. py:exception:: DataDirectoryException(error)

.. py:exception:: SignalException(signum)

.. py:module:: conreality.ddk.sysexits

Module ``conreality.ddk.sysexits``
----------------------------------

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
