************
Introduction
************

The Conreality Driver Development Kit (DDK) is a toolkit meant for hackers &
makers adding support in Conreality for new hardware devices or porting the
Conreality platform to new hardware architectures and development boards.

Conreality device drivers are userspace abstractions that are implemented
primarily in the C++ programming language.

The device drivers at this level do not generally deal with raw hardware
itself, but rather low-level system interfaces exposed by the kernel. For
example, the V4L2 video drivers for Linux are implemented using the
:manpage:`ioctl(2)` facility to communicate with the kernel-mode,
device-specific drivers that implement the V4L2 interface.
