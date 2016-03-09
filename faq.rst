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
