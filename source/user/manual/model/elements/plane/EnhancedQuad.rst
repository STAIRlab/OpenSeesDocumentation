
EnhancedQuad
^^^^^^^^^^^^

.. tabs::

   .. tab:: Python 

      .. function:: model.element("EnhancedQuad", tag, nodes, section, [pressure, rho, b1, b2])
         :noindex:

         :param tag: integer, unique element object tag
         :param nodes: tuple, a tuple of four element nodes in counter-clockwise order
         :param section: tuple or int. If int, it is the tag of a previously defined :ref:`PlaneSection`. If tuple, it is a tuple of the form (``thick``, ``type``, ``material``) where 
           
             ===================================   ==============================================================================================================
             ``thick`` |float|                     element thickness
             ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``
             ``material`` |integer|                tag of an :ref:`nDMaterial`
             ===================================   ==============================================================================================================
           
         :param pressure: |float|, surface pressure (optional, default = 0.0)
         :param rho: |float|, element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
         :param b1: |float|, constant body forces defined in the domain (optional, default=0.0)
         :param b2: |float|, constant body forces defined in the domain (optional, default=0.0)


   .. tab:: Tcl

      .. function:: element quad $eleTag $iNode $jNode $kNode $lNode $thick $type $matTag <$pressure $rho $b1 $b2>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $eleTag, |integer|, unique element object tag
         $iNode $jNode $kNode $lNode, |integer|   four nodes defining element boundaries, input in counter-clockwise order around the element.
         $thick, |float|,  element thickness
         $type, |string|,  string representing material behavior. The type parameter can be either "PlaneStrain" or "PlaneStress."
         $matTag, |integer|, tag of nDMaterial
         $pressure, |float|, surface pressure (optional: default = 0.0)
         $rho, |float|,  element mass density (per unit volume) from which a lumped element mass matrix is computed (optional: default=0.0)
         $b1 $b2, |float|, constant body forces defined in the isoparametric domain (optional: default=0.0)


Theory 
------

This element implements the Q1/E4 assumed strain interpolation. The formulation 
is generally credited to Taylor, Beresford, and Wilson (1976) [1]_. A variational basis 
for the formulation is given by Simo and Rifai (1990) [2]_.

.. math::

    \mathbf{M}_{\xi}=\left[\begin{array}{llll}
    \xi & 0 & 0 & 0 \\
    0 & \eta & 0 & 0 \\
    0 & 0 & \xi & \eta
    \end{array}\right]

For linear-elastic response, the formulation is equivalent to a Hellinger-Reissner element [3]_ with interpolation 

.. math::

    \mathbf{P}_{\xi}=\left[\begin{array}{cccccccc}
    1 & 0 & 0 & \eta & 0 & \xi \eta & 0 & 0 \\
    0 & 1 & 0 & 0 & \xi & 0 & \xi \eta & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & \xi \eta
    \end{array}\right]


References 
----------

.. [1] Taylor, R. L., Beresford, P. J., and Wilson, E. L. (1976). A nonconforming element for stress analysis. International Journal for Numerical Methods in Engineering, 10(6), 1211-1219.
.. [2] Simo, J. C., and Rifai, M. S. (1990). A class of mixed assumed strain methods and the method of incompatible modes. International Journal for Numerical Methods in Engineering, 29(8), 1595-1638.
.. [3] U. Andelfinger, E. Ramm (1993). EAS-elements for two-dimensional, three-dimensional, plate and shell structures and their equivalence to HR-elements.  https://doi.org/10.1002/nme.1620360805
.. [4] Armero, F (2008). Assumed strain finite element methods for conserving temporal integrations in non-linear solid dynamics. https://doi.org/10.1002/nme.1620330705