Radau
^^^^^

Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic
hinge integration methods.

Places ``N`` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on
numerical analysis. The force-deformation response at each integration point is defined
by the section. The order of accuracy for Gauss-Radau integration is :math:`2N-2`.

.. function:: beamIntegration "Radau" tag secTag N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$tag",       "|integer|",    "Unique object tag"
   "$sectTag",   "|integer|",    "A previous-defined section"
   "$N",         "|integer|",    "Number of Integration Points along the elementa"
   

Examples
--------

The following examples demonstrate the command in Tcl and Python script to add a Radau beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

.. tabs::
   
   .. tab:: Tcl

      .. code-block:: tcl

         beamIntegration "Radau" 2 1 6


   .. tab:: Python

      .. code-block:: python

         model.beamIntegration("Radau",2,1,6)


