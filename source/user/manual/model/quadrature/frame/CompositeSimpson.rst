
CompositeSimpson
^^^^^^^^^^^^^^^^

Create a CompositeSimpson beamIntegration.

.. function:: beamIntegration "CompositeSimpson" tag secTag N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$tag",       "|integer|",    "Unique object tag"
   "$sectTag",   "|integer|",    "A previous-defined section"
   "$N",         "|integer|",    "Number of Integration Points along the elementa"
   

Example
-------

The following examples demonstrate the command in Tcl and Python script to add a CompositeSimpson beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration "CompositeSimpson" 2 1 6


2. **Python Code**

   .. code-block:: python

      model.beamIntegration("CompositeSimpson",2,1,6)







