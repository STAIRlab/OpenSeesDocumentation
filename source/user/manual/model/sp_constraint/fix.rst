.. _fix:

fix Command
^^^^^^^^^^^

This command is used to construct a number of single-point homogeneous boundary constraints.

.. tabs::

   .. tab:: Python

      .. py:function:: model.fix(node, [flags, dof])

         :param node: integer tag identifying the node to be constrained
         :param flags: tuple of ``ndf`` constraint flags (``0`` or ``1``) corresponding to the ``ndf`` degrees-of-freedom.
            ``0`` unconstrained (or free)
            ``1`` constrained (or fixed)
         :param dofs: An alternative to the ``flags`` argument, the ``dofs`` argument allows specific degrees of freedom to be fixed.


   .. tab:: Tcl

      .. function:: fix $node $flags...

      .. program:: fix
      
      .. option:: -dof <dof>

         Specify a single degree of freedom to fix.

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $node, |integer|, unique tag identifying the node to be constrained
         $flags, |listInt|, "| ndf constraint values (0 or 1) corresponding to the ndf 
         | degrees-of-freedom.
         | 0 unconstrained (or free)
         | 1 constrained (or fixed)"


Example 
-------

The following examples demonstrate the commands in a script to add homogeneous boundary conditions
to nodes **1** and **2** for a model with **ndf** of 6. Node **1** is specified to be totally fixed, node **2** is only constrained in the second and fifth degree-of-freedom.

.. tabs::
   .. tab:: Python (``flags``)

      .. code-block:: none

         model.fix(1, (1,1,1,1,1,1)) 
         model.fix(2, (0,1,0,0,1,0)) 

   .. tab:: Python (``dofs``)

      .. code-block:: none

         model.fix(1, dofs=[1,2,3,4,5,6]) 
         model.fix(2, dofs=[2,5])
   
   .. tab:: Tcl


      .. code-block:: none

         fix 1 1 1 1 1 1 1 
         fix 2 0 1 0 0 1 0 

Code developed by: |fmk|