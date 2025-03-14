.. _getTime:

getTime
^^^^^^^


.. tabs::

   .. tab:: Python

      .. py:method:: Model.getTime()

         Return the current time in the :class:`Model`.

         :returns: |float| -- Current time.

   .. tab:: Tcl

      .. function:: getTime;

Example 
-------

The following example is used to set the variable **currentTime** to current state of **time** in the **Domain**

1. **Tcl Code**

   .. code-block:: tcl

	set currentTime [getTime]

2. **Python Code**

   .. code-block:: python

	currentTime = model.getTime()


Code developed by: |fmk|

