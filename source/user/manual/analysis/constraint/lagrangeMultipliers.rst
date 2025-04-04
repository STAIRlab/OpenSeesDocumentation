.. _lagrangeHandler:

Lagrange
^^^^^^^^

A *Lagrange* constraint handler enforces the constraints in a model by introducing Lagrange multipliers to the system of equation. 

.. function:: constraints Lagrange <$alphaS $alphaM >

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

     $alphaS, |float|,	 :math:`\alpha_S` factor on singe points. optional: default = 1.0
     $alphaM, |float|,	 :math:`\alpha_M` factor on multi-points. optional: default = 1.0

.. warning::

   The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. 
   This ensure that the system **IS NOT** symmetric positive definite and so do not use a positive definite solver.

Example 
-------

The following example shows how to construct a Lagrange constraint handler

1. **Tcl Code**

   .. code-block:: tcl

      numberer Lagrange


2. **Python Code**

   .. code-block:: python

      model.numberer('Lagrange')

Code Developed by: |fmk|

