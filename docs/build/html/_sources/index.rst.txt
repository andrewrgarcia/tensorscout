Welcome to tensorscout's documentation!
=======================================

What if for some reason, you could unlock 100% of your computing processing power?
-------------------------------------------------------------------------------------

.. |icon| image:: ../img/icon_scout.png
  :width: 100
  :alt: Alternative text
  :target: https://github.com/andrewrgarcia/tensorscout




|icon|


The Python package is designed for tensor operations and is optimized for parallel processing. 

One of the key features of this package is its support for parallel processing. 
It includes decorators powered by `pathos <https://pathos.readthedocs.io>`_ that allow users to distribute operations over multiple CPU cores or vCPUs
(with cloud computing), 
significantly reducing the time required for computation. Specifically, these decorators allow users to partition arrays into sectors and allocate 
operations for each sector over the defined available cores. The package currently does not include support for GPUs for faster processing, 
thought it may be a desired feature for the future. 

Overall, this package is ideal for users working with large-scale tensor operations and seeking to optimize performance through parallel processing.


Check out the :doc:`usage` section for further information, including how to :ref:`installation` the project. 


.. image:: ../img/parallel16.png
  :width: 300
  :alt: Alternative text




Colab Notebook
..............................

In progress

.. image:: ../img/colaboratory.png
  :width: 500
  :alt: Alternative text


.. note::

   This project is under active development.


Contents
--------

.. toctree::

   usage
   api


