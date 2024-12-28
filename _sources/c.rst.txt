New Page Title
===============

This is the content of your new page.

*   Bullet point 1
*   Bullet point 2

.. code-block:: python

    def my_function():
        print("Hello from the new page!")

**3. Add the new page to the toctree:**

*   Open the `index.rst` (or your main toctree file) and add the new page to the `toctree` directive:

```rst
.. toctree::
   :maxdepth: 2

   new_page 