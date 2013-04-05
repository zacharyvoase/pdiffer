pdiffer
=======

A Python interface to the
```perceptualdiff`` <http://pdiff.sourceforge.net/>`__ tool, plus
helpers for making pdiff-based assertions in tests. By
`Zack <http://zacharyvoase.com/>`__.

Install using pip:

::

    pip install pdiffer

You need to have ``perceptualdiff`` installed somewhere on your computer
for this library to work.

Usage
-----

Create your ``PDiffer`` instance, optionally specifying a path to the
binary:

.. code:: python

    from pdiffer import PDiffer
    pdiff = PDiffer(bin='/usr/local/bin/perceptualdiff')
    # or, just
    from pdiffer import pdiff

Diff two images by pathname:

.. code:: python

    result = pdiff('image1.png', 'image2.png')

If the images are similar enough, ``result`` will be falsy; that is, the
following code will print 'SAME':

.. code:: pycon

    >>> if result:
    ...     print 'DIFFERENT'
    ... else:
    ...     print 'SAME'
    SAME

You can get the string output of the command by just calling
``unicode``/``str`` (or even ``print``) on the result:

.. code:: pycon

    >>> print(result)
    PASS: Images are binary identical

If the images are different, you'll see something else:

.. code:: pycon

    >>> result = pdiff('image1.png', 'image3.png')
    >>> if result:
    ...     print(result)
    FAIL: Image dimensions do not match

Parameters
~~~~~~~~~~

There are a few parameters you can customize in the pdiff invocation:

.. code:: python

    pdiff('image1.png', 'image2.png',
        fov=65,
        threshold=40,
        gamma=2.2,
        luminance=100,
        luminanceonly=True,
        colorfactor=1.0,
        downsample=0,
        output='o.ppm')

Documentation on all of these options can be found by running
``perceptualdiff -help``.

Test Assertions
~~~~~~~~~~~~~~~

PerceptualDiff is mostly useful in automated testing, and therefore some
basic assertions are provided for checking image similarity (under both
PEP8 and camelCase names):

.. code:: python

    from pdiffer import assertImagesSimilar, assertImagesDifferent
    from pdiffer import assert_images_similar, assert_images_different


    def test_something():
        assert_images_different('image1.png', 'image2.png')
        assert_images_similar('image1.png', 'image3.png')

These assertions take parameters just like ``pdiff()``, e.g.:

.. code:: python

    assert_images_different('image1.png', 'image2.png', fov=89.9, threshold=40)

Unlicense
---------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of
this software dedicate any and all copyright interest in the software to
the public domain. We make this dedication for the benefit of the public
at large and to the detriment of our heirs and successors. We intend
this dedication to be an overt act of relinquishment in perpetuity of
all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

For more information, please refer to http://unlicense.org/
