.. _ManzariDafalias:

Manzari Dafalias
^^^^^^^^^^^^^^^^

Code Developed by: **Alborz Ghofrani**, |pedro|, U. Washington

This command is used to construct a multi-dimensional [Manzari-Dafalias2004]_ material.

.. function:: nDmaterial ManzariDafalias $matTag $G0 $nu $e_init $Mc $c $lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $z_max $cz $Den

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   tag, |integer|,	unique tag identifying material
   G0, |float|, 	   shear modulus constant
   nu, |float|, 	   poisson ratio
   e_init, |float|, initial void ratio
   Mc, |float|, 	   critical state stress ratio
   c, |float|, 	   ratio of critical state stress ratio in extension and compression
   lambda_c, |float|, critical state line constant
   e0, |float|, critical void ratio at p = 0
   ksi, |float|, critical state line constant
   P_atc, |float|, atmospheric pressure
   m, |float|, yield surface constant (radius of yield surface in stress ratio space)
   h0, |float|, constant parameter
   ch, |float|, constant parameter
   nb, |float|, bounding surface parameter  $nb ≥ 0
   A0, |float|, dilatancy parameter
   nd, |float|, dilatancy surface parameter $nd ≥ 0
   z_max, |float|, fabric-dilatancy tensor parameter
   cz, |float|, fabric-dilatancy tensor parameter
   Den, |float|, mass density of the material

.. note::

   The material formulations for the Manzari-Dafalias object are "ThreeDimensional" and "PlaneStrain"


#. Valid Element Recorder queries are:

   * ``stress``, ``strain``
   * ``alpha`` (or backstressratio) for :math:`\mathbf{\alpha}`
   * ``fabric`` for :math:`\mathbf{z}`
   * ``alpha_in`` for :math:`\mathbf{\alpha_{in}}`

   For example,

   .. code-block:: tcl

      recorder Element -eleRange 1 $numElem -time -file stress.out  stress

#. Elastic or Elastoplastic response could be enforced by

   .. code-block:: tcl

      updateMaterialStage -material $matTag -stage 0; # Elastic
      updateMaterialStage -material $matTag -stage 1; # Elastoplastic


Theory
------

.. math::

   p = \frac{1}{3} \mathrm{tr}(\mathbf{\sigma}) 


.. math::
   
    \mathbf{s} = \mathrm{dev} (\mathbf{\sigma}) = \mathbf{\sigma} - \frac{1}{3} p \mathbf{1} 


Elasticity
""""""""""

Elastic moduli are considered to be functions of :math:`p` and current void ratio:

.. math::

   G = G_0 p_{atm}\frac{\left(2.97-e\right)^2}{1+e}\left(\frac{p}{p_{atm}}\right)^{1/2}

.. math:: 

   K = \frac{2(1+\nu)}{3(1-2\nu)} G

The elastic stress-strain relationship is:

.. math:: 

   d\mathbf{e}^\mathrm{e} = \frac{d\mathbf{s}}{2G}


.. math:: 

   d\varepsilon^\mathrm{e}_v = \frac{dp}{K}


Critical State Line
"""""""""""""""""""
A power relationship is assumed for the critical state line:

.. math:: 

   e_c = e_0 - \lambda_c\left(\frac{p_c}{p_{atm}}\right)^\xi

where :math:`e_0` is the void ratio at :math:`p_c = 0` and :math:`\lambda_c` and :math:`\xi` constants.


Yield Surface
"""""""""""""

Yield surface is a stress-ratio dependent surface in this model and is defined as

.. math::

   \left\| \mathbf{s} - p \mathbf{\alpha} \right\| - \sqrt\frac{2}{3}pm = 0 

with :math:`\mathbf{\alpha}` being the deviatoric back stress-ratio.

Plastic Strain Increment
""""""""""""""""""""""""

The increment of the plastic strain tensor is given by

.. math:: 

   d\mathbf{\varepsilon}^p = \langle L \rangle \mathbf{R}

where

.. math::

   \mathbf{R} = \mathbf{R'} + \frac{1}{3} D \mathbf{1}

therefore

:math:`d\mathbf{e}^p = \langle L \rangle \mathbf{R'}` and :math:`d\varepsilon^p_v = \langle L \rangle D`
The hardening modulus in this model is defined as

.. math::
 
 K_p = \frac{2}{3} p h (\mathbf{\alpha}^b_{\theta} - \mathbf{\alpha}): \mathbf{n}

where :math:`\mathbf{n}` is the deviatoric part of the gradient to yield surface.

.. math::

   \mathbf{\alpha}^b_{\theta} = \sqrt{\frac{2}{3}} \bigl( g(\theta,c) M_c \exp(-n^b \Psi) - m\bigr) \mathbf{n}

where :math:`\Psi` is the state parameter. The hardening parameter :math:`h` is defined as

.. math:: 

   h \triangleq \frac{b_0}{(\mathbf{\alpha}-\mathbf{\alpha_{in}}):\mathbf{n}}

where :math:`\mathbf{\alpha_{in}}` is the value of :math:`\mathbf{\alpha}` at initiation of loading cycle.

.. math::

   b_0 = G_0 h_0 (1-c_h e) \left(\frac{p}{p_{atm}}\right)^{-1/2}

Also the dilation parameters are defined as

.. math:: 

   D = A_d (\mathbf{\alpha}^d_{\theta}-\mathbf{\alpha}) : \mathbf{n}

.. math:: 

   \mathbf{\alpha}^d_{\theta} = \sqrt{\frac{2}{3}} \left[g(\theta,c) M_c \exp(n^d \Psi) - m\right] \mathbf{n}


.. math:: 
   
   A_d = A_0 (1+\langle \mathbf{z}:\mathbf{n}\rangle) 

where :math:`\mathbf{z}` is the fabric tensor.

The evolution of fabric and the back stress-ratio tensors are defined as

.. math:: 
 
 d\mathbf{z} = - c_z \langle -d\varepsilon^p_v \rangle (z_{max}\mathbf{n}+\mathbf{z})`

.. math::

   d\mathbf{\alpha} = \langle L \rangle (2/3) h (\mathbf{\alpha}^b_{\theta} - \mathbf{\alpha})



Example
-------

This example, provides an undrained confined triaxial compression test using one 8-node SSPBrickUP element and ManzariDafalias material model.

.. literalinclude:: ManzariDafaliasExample.tcl
   :language: bash


References
----------

.. [Manzari-Dafalias2004] Dafalias YF, Manzari MT. "Simple plasticity sand model accounting for fabric change effects". Journal of Engineering Mechanics 2004

