.. _penalty:

Penalty
^^^^^^^

The PenaltyMethod constraint handler enforces the constraints by using the *penalty* method. 

.. function:: constraints Penalty $alphaS $alphaM

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

     $alphaS, |float|,	 :math:`\alpha_S` factor on singe points. 
     $alphaM, |float|,	 :math:`\alpha_M` factor on multi-points. 


.. warning::

   The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).

Example 
-------

The following example shows how to construct a Penalty Method constraint handler

1. **Tcl Code**

   .. code-block:: tcl

      numberer Penalty 1.0e10 1.0e10


2. **Python Code**

   .. code-block:: python

      model.numberer("Penalty", 1.0e10, 1.0e10)

Code Developed by: |fmk|
