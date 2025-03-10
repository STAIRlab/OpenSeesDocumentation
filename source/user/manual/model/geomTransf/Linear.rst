.. _linearTR:

Linear
^^^^^^

This command is used to construct a linear coordinate transformation, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system.

.. tabs::

   .. tab:: Python

      .. py:function:: model.geomTransf("Linear", tag, vecxz, [offi, offj])

         :param integer tag: integer tag identifying transformation
         :type tag: int
         :param vecxz: X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system, **required in 3D**. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         :type vecxz: tuple of floats
         :param offi: joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model).
         :type offi: tuple of floats
         :param offj: joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model).
         :type offj: tuple of floats

   .. tab:: Tcl
      .. function:: geomTransf Linear $transfTag < $vecxzX $vecxzY $vecxzZ > <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $transfTag, |integer|, integer tag identifying transformation
         $vecxzX $vecxzY $vecxzZ,  |float|,  "X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         
         These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
         
         These items need to be specified for the three-dimensional problem."
         $dXi $dYi $dZi, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model)."
         $dXj $dYj $dZj, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model)."

Notes 
-----

Recall that any 2 vectors, :math:`\mathbf{i}_1` and :math:`\mathbf{i}_2`, not parallel, define a plane that is parallel to them both. 
The cross-product of these vectors define a third vector, :math:`V_t`, that is perpendicular to both :math:`\mathbf{i}_1` and :math:`\mathbf{i}_2` and hence normal to the plane: :math:`\mathbf{i} = \mathbf{i}_1 \times \mathbf{i}_2`.


The longitudinal basis vector :math:`\mathbf{i}` derived from the two element end nodes. 
The vector **vecxz** is a vector the user specifies that must not be parallel to the longitudinal (:math:`x`) axis. 
The x-axis along with the **vecxz** Vector define the xz plane. The local y-axis is defined by taking the cross product of the x-axis vector and the **vecxz** vector (:math:`\mathbf{i}_y = V_{xz} \times \mathbf{i}`). 
The local z-axis is then found simply by taking the cross product of the y-axis and x-axis vectors (:math:`\mathbf{i}_z = \mathbf{i} \times \mathbf{i}_y`). 
The section is attached to the element such that the y-z coordinate system used to specify the section corresponds to the y-z axes of the element.

.. figure:: figures/ElementOrentation.gif
	:align: center
	:width: 600px
	:figclass: align-center

	Element Orentation

.. figure:: figures/RigidElementOffsets.gif
	:align: center
	:width: 600px
	:figclass: align-center

	Rigid Element Offsets


.. note::

	When in 2D, local x and y axes are in the X-Y plane, where X and Y are global axes. Local x axis is the axis connecting the two element nodes, and local y and z axes follow the right-hand rule (e.g., if the element is aligned with the positive Y axis, the local y axis is aligned with the negative X axis, and if the element is aligned with the positive X axis, the local y axis is aligned with the positive Y axis). Orientation of local y and z axes is important for definition of the fiber section.


Example
-------

In the following, the linear transformtion commands are provided for the elements shown in the figures.

.. figure:: figures/ElementCrossSection.png
	:align: center
	:width: 400px
	:figclass: align-center

	Elements Cross Section

.. figure:: figures/ElementOrientation.png
	:align: center
	:width: 400px
	:figclass: align-center

	Elements Orientation

.. figure:: figures/ElementVectors.png
	:align: center
	:width: 400px
	:figclass: align-center

	Elements Vectors		

1. **Tcl Code**

   .. code-block:: tcl

	#Element 1 : tag 1 : vecxZ = zaxis
	geomTransf Linear 1 0 0 -1

	#Element 2 : tag 2 : vecxZ = y axis
	geomTransf Linear 2 0 1 0

	#If there was a rigid offset at the top of element 1:
	geomTransf Linear 1 0 0 -1 -jntOffset 0.0 0.0 0.0 0.0 -$Offset 0.0


2. **Python Code**

   .. code-block:: python
   
	# Element 1, vecxZ = zaxis
	geomTransf('Linear', 1, (0, 0, -1))

	# Element 2, vecxZ = y axis
	geomTransf('Linear', 2, (0, 1,  0))

	#If there was a rigid offset at the top of element 1: (offset is a variable that the offset value has been stored in)
	geomTransf('Linear', 3, 0, 0, -1,'-jntOffset',0.0, 0.0, 0.0, 0.0, offset, 0.0)	


| Code Developed by: Remo Magalhaes de Souza 
| Images Developed by: |silvia|
