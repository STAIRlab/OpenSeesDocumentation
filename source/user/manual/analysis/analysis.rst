.. _analysis:

analysis
^^^^^^^^

This is the command issued to create an analysis.

.. tabs::

   .. tab:: Python

      .. function:: model.analysis(type, *args)

   .. tab:: Tcl

      .. function:: analysis type? <-numSublevels $x -numSubSteps $y>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   ``type``, |string|, type of analysis object to be constructed. Currently 3 valid options:
   , ,  **Static** - for static analysis
   , ,  **Transient** - for transient analysis with constant time step
   , ,  **VariableTransient** - for transient analysis with variable time step
   ``x``, |integer|, number of sublevels transient analysis should try if failure
   ``y``, |integer|, number of subdivisions to be tried at each sublevel


.. toctree::

   static
   transient

.. note::

   The ``<-numSublevels $x -numSubSteps $y>`` only works for the **Transient** type

   The components of the analysis, i.e. numberer, constraint handler, system, test, integrator, algorithm, should all be issued BEFORE the analysis object is created.

   The **VariableTransient** option is still available. The optional additions for the Transient analysis have been found to provide better options for nonlinear problems with convergence issues.


.. warning::

   When switching from one type of analysis to another, e.g. ``Static`` to ``Transient``, it is necessary to issue a :ref:`wipeAnalysis`.


Static Analysis Example
-----------------------

The following example shows how to construct a Static analysis.

1. **Tcl Code**

.. code:: tcl

   system SuperLU
   constraints Transformation
   numberer RCM
   test NormDispIncr 1.0e-12  10 3
   algorithm Newton
   integrator LoadControl 0.1
   analysis Static


2. **Python Code**

.. code:: python

   model.system("SuperLU")
   model.constraints("Transformation")
   model.numberer("RCM")
   model.test("NormDispIncr", 1.0e-12, 10, 3)
   model.algorithm("Newton")
   model.integrator("LoadControl", 0.1)
   model.analysis("Static")


Transient Analysis Example
--------------------------

The following example shows how to construct a Transient analysis.

1. **Tcl Code**

.. code:: tcl

   system SuperLU
   constraints Transformation
   numberer RCM
   test NormDispIncr 1.0e-12  10 3
   algorithm Newton
   integrator Newmark 0.5 0.25
   analysis Transient -numSubLevels 3  -numSubSteps 10


2. **Python Code**

.. code:: python

   model.system("SuperLU")
   model.constraints("Transformation")
   model.numberer("RCM")
   model.test("NormDispIncr", 1.0e-12, 10, 3)
   model.algorithm("Newton")
   model.integrator("Newmark", 0.5, 0.25)
   model.analysis("Transient")


Code Developed by |fmk|
