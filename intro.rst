************
Introduction
************

Conreality device drivers are userspace abstractions that are implemented
primarily in the OCaml programming language, with minor bits of lower-level
C/C++ language glue as needed.

The device drivers at this level do not generally deal with raw hardware
itself, but rather low-level system interfaces exposed by the kernel. For
example, the V4L2 video drivers for Linux are implemented using the
:manpage:`ioctl(2)` facility to communicate with the kernel-mode,
device-specific drivers that implement the V4L2 interface.
