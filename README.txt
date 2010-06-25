hurry.raphael
*************

Introduction
============

This library packages Raphael_ for `hurry.resource`_. It is aware of Raphael's
structure and different modes (normal, minified).

.. _`hurry.resource`: http://pypi.python.org/pypi/hurry.resource
.. _Raphael: http://raphaeljs.com/

How to use?
===========

You can import Raphael from ``hurry.raphael`` and ``.need`` it where you want
these resources to be included on a page::

  from hurry import raphael

  .. in your page or widget rendering code, somewhere ..

  raphael.need()

This requires integration between your web framework and ``hurry.resource``,
and making sure that the original resources (shipped in the ``raphael-build``
directory in ``hurry.raphael``) are published to some URL.

The package has already been integrated for Grok_ and Zope 3. If you depend
on the `hurry.zoperesource`_ package in your ``setup.py``, the above example
should work out of the box. Make sure to depend on the `hurry.zoperesource`_
package in your ``setup.py``.
For grok, depending on `megrok.resource`_ should do it

.. _`hurry.zoperesource`: http://pypi.python.org/pypi/hurry.zoperesource
.. _`megrok.resource`: http://pypi.python.org/pypi/megrok.resource
.. _Grok: http://grok.zope.org

Preparing hurry.raphael before release
======================================

This section is only relevant to release managers of ``hurry.raphael``.

When releasing ``hurry.raphael``, an extra step should be taken. Follow the
regular package `release instructions`_, but before egg generation (``python
setup.py register sdist upload``) first execute ``bin/raphaelprepare``. This
will download the Raphael library and place it in the egg.  (The version number
is currently hardcoded in the hurry.raphael.prepare module).

.. _`release instructions`: http://grok.zope.org/documentation/how-to/releasing-software
