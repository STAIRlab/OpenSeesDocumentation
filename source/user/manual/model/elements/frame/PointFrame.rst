ZeroLength Section Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a zero length element, which is defined by two nodes at the same location. 
The nodes are connected by a single section object to represent the force-deformation relationship for the element.

.. tabs::
   
   .. tab:: Python

      .. py:method:: Model.element("PointFrame", tag, nodes, section, *args, **kwargs)
         :no-index:

         :param tag: integer tag identifying the element
         :type tag: |integer|
         :param nodes: tuple of integer tags identifying the nodes that form the element (see :ref:`node`)
         :type nodes: tuple
         :param section: integer tag identifying a :ref:`section`.
         :type section: |integer|
         :param args: optional arguments
         :param kwargs: optional keyword arguments

   .. tab:: Tcl

      .. function:: element PointFrame $tag $iNode $jNode $secTag <-orient $x1 $x2 $x3 $yp1 $yp2 $yp3> <-doRayleigh $rFlag>

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, unique :ref:`Element` tag
         $nodes, |integerList|, 2 end nodes
         $secTag, |integer|, tag associated with previously-defined Section object
         $x,  |floatList|,  (optional) 3 components in global coordinates defining local x-axis 
         $yp, |floatList|, "| (optional) 3 components in global coordinates defining vector yp 
         | which lies in the local x-y plane for the element."
         $rFlag, |integer|, "| optional, default = 0
         | rFlag = 0 NO RAYLEIGH DAMPING (default)
         | rFlag = 1 include rayleigh damping"


.. note::

   If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

   The section force-deformation response represented by section string P acts along the element local x-axis, and the response for code Vy along the local y-axis. The other modes of section response follow from this orientation.


.. warning::

   If the distance between end noes is not **0.0** a warning message will appear when the script is run. This is just a warning in case you have made a mistake as most users when they use zeroLength elements are wanting to use them in the more normal way. ZeroLength elements can be used between nodes with non-zero length.


Recorders 
---------

The valid queries to a zero-length element when creating an ElementRecorder object are 

#. ``"force"``, ``"deformation"``, ``"stiff"``, and ``"section $args ..."``.


Example
------- 

The following examples demonstrate the commands in a script to add three zeroLength elements to domain. The three to be added have element tags **1**, **2**, and **3**. Element **1** has nodes **2** and **3** as its end ndes, has two materials **5** and **6** acting in directions **1** and **2**. Element **2** has as its end nodes **4** and **5**, has only one material **1** acting in direction **1**, the element has a global orientation.

1. **Tcl Code**

   .. code-block:: none

      element PointFrame 1 2 4 6
      element PointFrame 2 4 5 6 -orient 1 1 0 -1 1 0
      element PointFrame 2 4 5 6 -orient 1 1 0 -1 1 0 -doRayleigh 1



Code Developed by: |mhs|
