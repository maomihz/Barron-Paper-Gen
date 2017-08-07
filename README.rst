Barron Testpaper Generator
==========================

A command-line utility to generate a testpaper (wordlist) based on *Barron SAT 3500 Wordlist*.

============
Introduction
============

This is a Python command-line script to generate a testpaper (wordlist) based on *Barron SAT 3500 Wordlist*, although it can be used for any vocabulary list (bundle) properly formatted.

By changing the command line arguments, it can select specified number of random vocabularies from specified units. The vocabulary bundle is not included in the package and must be downloaded and installed seperately.

=============================
Installation
=============================

Currently the package is not published to PyPI yet, but you can still use pip to install. Python 3 is recommended although it also compatible with Python 2::

  pip install git+https://github.com/maomihz/Barron-Paper-Gen

You may need to prefix the command with ``sudo`` to install the executable to global binary directory.

Test the installation by running ``barron`` with no arguments::

  $ barron
  usage: barron [-h] [-n COUNT] [-o [OUTPUT]] [-i BUNDLE_ZIP [BUNDLE_ZIP ...]]
              [-r BUNDLE_NAME [BUNDLE_NAME ...]] [-l]
              [range]
  barron: error: Argument range is required

If it displays a simple help message then the installation is successful. If it shows command not found, you may need to consult the documentation of pip.

=============================
Setting Up Vocabulary Bundles
=============================

The script is not bundled with any vocabulary lists, so you need to download and install one first. See the end of this document for downloads. The vocabulary bundles are in zip files, to install them, run the following command::

  $ barron -i path/to/bundle.zip
  path/to/barron.zip installed to /home/example/.barron

Where ``path/to/bundle.zip`` is the path to the vocabulary zip file.

To list all the vocabulary bundles installed::

  $ barron -l
  === Installed Bundles: ===
  barron 1-50

To delete an installed vocabulary bundle, use ``-r``::

  $ barron -r barron

Bundle ``barron`` and installed files would be removed.

=========================
Generate Vocabulary Lists
=========================

To generate a test paper selected from specified bundle and unit, run the following command::

  $ barron [range]

The range selector is a comma-seperated string that specifies the units to select from a vocabulary bundle. You can put either a single number (``4``) or a range (``1-5``) as each element. An example would be ``1,2,3,5-10,12`` which selects unit 1-3, 5-10 and 12. They do not need to be in particular order.

Next the command would prompt for a vocabulary bundle to select. Enter the number and press enter.

Example::

  $ barron 1,2,3,5-10,12
  [0] barron
  Enter Selection (0) ==> 0
  # barron List 1-3,5-10,12

  001   cant
  002   bluff
  003   ceremonious
  ...

By default, the utility randomly selects 100 words and prints to the console screen.

====================
Specify More Options
====================

To change the number of words to select in the test, use ``-n``. In this example, the number of words would be 200::

  barron -n 200 1-3,5-10,12

Note that if there is not enough words available, all the words would be shuffled and printed.

To redirect the output to a file, use ``-o``::

  barron -o testpaper.txt 1-3,5-10,12

It would silently overwrite ``testpaper.txt`` and write randomly selected vocabulary instead of printing to the console. If ``-o`` is specified without an argument, the default file name ``barron_testpaper.txt`` would be used.

=================
Uninstall
=================

To remove the package from pip, run the following command::

  pip uninstall barron-gen


=====================
Development
=====================
This script package consists of following files:

* ``barron/`` - Main package

  * ``__init__.py``
  * ``__main__.py``
  * ``barron_testpaper_generator.py`` - Command line entry
  * ``barron.py`` - Essential libraries

* ``setup.py`` - pip setup file
* ``README.rst`` - This help manual
* ``MANIFEST.in`` - pip extra file specification
* ``LICENSE`` - The license the script uses

To start development, clone the repository::

  git clone https://github.com/maomihz/Barron-Paper-Gen
  cd Barron-Paper-Gen

It is recommended to install the package first so it is easier to run the command::

  pip install -e .

Make sure you are in the root directory when run the above command. ``-e`` option allows the source file to be changed without reinstalling. Simply run ``barron`` again to reflect the change in code.

It is also possible to run without installing::

  python -m barron
  python -m barron.barron_testpaper_generator

Either of the above command runs the module directly. 

=====================
Copyright
=====================
  The MIT License (MIT)

  Copyright (c) 2017 Hisen Zhang

  Copyright (c) 2017 Dexter MaomiHz

  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

=========
Downloads
=========

All the following files are for **Personal and Educational Use Only!!!** By downloading you are responsible for the usage of these files.

- Barron 3500 Word List: `#1 <https://github.com/maomihz/Barron-Paper-Gen/issues/1>`_
