********************************
Frequently Asked Questions (FAQ)
********************************

**(To be written.)**

Technical Questions
===================

What user privileges do the device drivers require?
---------------------------------------------------

Drivers generally require superuser privileges. The reason varies per
driver: for example, the Sysfs drivers for GPIO manipulate virtual files in
the :file:`/sys/class/gpio` VFS hierarchy on Linux, which requires ``root``
privileges; meanwhile, the BCM283x drivers for GPIO require access to
:file:`/dev/mem` in order to perform :term:`DMA` operations, which also
requires ``root``.

Could drivers be written in Java or other JVM languages?
--------------------------------------------------------

Drivers can be written in any programming language capable of producing
executable scripts or binaries that can be run as subprocesses of the
Conreality daemon. However, given the :abbr:`JVM (Java Virtual Machine)`'s
startup time and memory overhead, JVM-based languages, such as Java, would
be ill-suited for writing drivers.
