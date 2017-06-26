**********************************************
Conreality Driver Development Kit (DDK) Manual
**********************************************

.. image:: https://img.shields.io/badge/license-Public%20Domain-blue.svg
   :alt: Project license
   :target: https://creativecommons.org/publicdomain/zero/1.0/

.. image:: https://img.shields.io/travis/conreality/ddk.conreality.org/master.svg
   :alt: Travis CI build status
   :target: https://travis-ci.org/conreality/ddk.conreality.org

|

This is the source repository for the
`Conreality Driver Development Kit (DDK) <https://ddk.conreality.org/>`__
manual and website.

*All materials herein are released into the
`public domain <https://creativecommons.org/publicdomain/zero/1.0/>`__.*

Prerequisites
=============

The following software is required in order to build this manual from source:

* `Python
  <https://www.python.org/downloads/>`__
  3.5+
* `Sphinx
  <https://pypi.python.org/pypi/Sphinx>`__
  1.6.2+
* `Sphinx Bootstrap Theme
  <https://pypi.python.org/pypi/sphinx-bootstrap-theme/>`__
  0.5.3+
* `Graphviz
  <http://www.graphviz.org/Download..php>`__

::

   $ pip3 install -U sphinx
   $ pip3 install -U sphinx_bootstrap_theme

   $ brew install graphviz      # on macOS
   $ sudo apt install graphviz  # on Ubuntu or Debian Linux

Building the Manual
===================

::

   $ make html      # HTML output in .build/html/index.html
   $ make latexpdf  # PDF  output in .build/latex/conreality-ddk.pdf
   $ make epub      # EPUB output in .build/epub/conreality-ddk.epub

Publishing the Manual
=====================

::

   $ make clean html publish
