******************
ddk.conreality.org
******************

This is the source repository for the
`Conreality DDK documentation <http://ddk.conreality.org/>`__ website.

All materials herein are released into the
`public domain <https://creativecommons.org/publicdomain/zero/1.0/>`__.

Prerequisites
=============

::

   $ pip install -U sphinx
   $ pip install -U sphinx_bootstrap_theme

Building the Manual
===================

::

   $ make html      # HTML output in .build/html/index.html
   $ make latexpdf  # PDF output in .build/latex/conreality-ddk.pdf
   $ make epub      # EPUB output in .build/epub/conreality-ddk.epub

Publishing the Manual
=====================

::

   $ make clean html publish
