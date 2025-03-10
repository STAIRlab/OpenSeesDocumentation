.. _numberer:

numberer
********

This command is used to construct the **DOF_Numberer** object. 
The **DOF_Numberer** object determines the mapping between equation numbers in the system of equations and the degrees-of-freedom at the nodes, basically how degrees-of-freedom are numbered.

.. function:: numberer type arg1? ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
	$numbererType, |string|,  the numberer type
	$args, |list|,   a list of arguments for that type


The following contain information about ``type`` and the args required for each of the available dof numberer types:

.. toctree::

    numberer/PlainNumberer
    numberer/RCM
    numberer/AMD

Code developed by: |fmk|
