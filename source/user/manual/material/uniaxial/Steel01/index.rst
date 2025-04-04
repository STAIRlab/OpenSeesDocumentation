.. _steel01:

Steel01
^^^^^^^

This model implements a uniaxial bilinear steel material object with kinematic hardening and optional isotropic hardening described by a non-linear evolution equation (REF: Fedeas).

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.uniaxialMaterial("Steel01", tag, fy, E0, b, [a1, a2, a3, a4])
         :no-index:

         :param int tag: integer tag identifying material
         :param |float| fy: yield strength
         :param |float| E0: initial elastic tangent
         :param |float| b: strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
         :param |float| a1: optional: isotropic hardening parameter: increase of compression yield envelope as proportion of yield strength after a plastic strain of ``a2*(fy/E0)``.
         :param |float| a2: optional: isotropic hardening parameter (see explanation under ``a1``)
         :param |float| a3: optional: isotropic hardening parameter: increase of tension yield envelope as proportion of yield strength after a plastic strain of ``a4*(Fy/E0)``
         :param float a4: optional: isotropic hardening parameter (see explanation under ``a3``)

   .. tab:: Tcl

      .. function:: uniaxialMaterial Steel01 $tag $Fy $E0 $b <$a1 $a2 $a3 $a4>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, integer tag identifying material
         $Fy, |float|, yield strength
         $E0, |float|, initial elastic tangent
         $b, |float|, strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
         $a1, |float|, optional: isotropic hardening parameter: increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0).
         $a2, |float|, optional:isotropic hardening parameter (see explanation under $a1)
         $a3, |float|, optional: isotropic hardening parameter: increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0)
         $a4, |float|, optional: isotropic hardening parameter (see explanation under $a3)



.. figure:: figures/Steel01.png
	:align: center
	:figclass: align-center

	Steel01 behaviour under cyclic loading.


Examples
--------

The following is used to construct a *Steel01* material with a tag of **1**, a yield strength of **60** and an initial tangent stiffness of **30,000**.

1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Steel01 60.0 30000.0

2. **Python Code**

   .. code-block:: python

      model.uniaxialMaterial("Steel01",60.0,30000.0)

Code Developed by: |fcf|, |mhs|

