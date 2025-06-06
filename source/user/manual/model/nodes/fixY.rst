fixY
^^^^

This command is used to construct multiple homogeneous single-point boundary constraints for all nodes whose :math:`y`-coordinate lies within a specified distance from a specified coordinate.

.. function:: fixY $y {*}$fixities <-tol $tol>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $yCoordinate, |float|, y-coordinate of nodes to be constrained
   $fixities, |listInt|, " | :py:attr:`Model.ndf` constraint values (0 or 1) corresponding to the ndf 
   | degrees-of-freedom.
   | 0 unconstrained (or free)
   | 1 constrained (or fixed) "
   $tol, |float|, user-defined tolerance (optional: default = 1e-10)

Example
-------

The following example demonstrate the command to fix the first 3 degrees-of-freedom at all nodes in the model at :math:`y` location **20.0**.

1. **Tcl Code**

   .. code-block:: none

      fixY 20.0 1 1 1 0 0 0 

2. **Python Code**

   .. code-block:: none

      model.fixY(20.0, (1, 1, 1, 0, 0, 0))

Code Developed by: **fmk**
