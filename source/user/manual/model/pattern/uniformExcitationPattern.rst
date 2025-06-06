.. _uniformExcitation:

Uniform Excitation
^^^^^^^^^^^^^^^^^^

The UniformExcitation pattern applies a uniform excitation to a model acting in specified directions. 


.. tabs::

   .. tab:: Python

      .. py:method:: Model.pattern("UniformExcitation", tag, dof, accel, vel0=0.0, fact=1.0)
         :no-index:

         :param |integer| tag: unique tag among load patterns
         :param |integer| dof: degree of freedom in the direction the ground motion acts
         :param |integer| accel: tag of the TimeSeries series defining the acceleration history.
         :param |float| vel0: the initial velocity (optional: default=0.0)
         :param |float| fact: constant factor (optional: default=1.0)
   
   .. tab:: Tcl

      .. function:: pattern UniformExcitation $tag $dof -accel $tsTag <-vel0 $vel0> <-fact $cFact>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, unique tag among load patterns
         $dof, |integer|, dof direction the ground motion acts
         $tsTag, |integer|, tag of the TimeSeries series defining the acceleration history.
         $vel0, |float|, the initial velocity (optional: default=0.0)
         $cFact, |float|, constant factor (optional: default=1.0)


.. warning::

   The responses obtained from the nodes for this type of excitation are **relative** values, and not the absolute values obtained from a :ref:`multisupportExcitation`. This is a consequence of the equation of motion being solved: 

   .. math::
   
	   M\ddot{\boldsymbol{u}} + C\dot{\boldsymbol{u}} + K \boldsymbol{u} = p(t)

   and how the loads are applied with this load pattern.

   .. math::

      p(t) = -c_{Fact} M l \ddot{u_g}

   where :math:`l` is a vector of **1**'s and **0**'s, with a **1** corresponding to all matrix equations in the **$dof** degree-of-freedom direction and **0** for all other degrees-of-freedom. 
   The :math:`\ddot u_g` is obtained from the time series.

Examples
--------

The following example shows how to construct a *UniformExcitation* pattern with a tag of **2** acting in the **1** direction. The acceleration for the pattern comes from the :ref:`pathTimeSeries` with tag **3** which has been created using the contents of the ``elCentro.dat`` file, a :math:`\delta t = 0.02`, and a scale factor given by the variable **g**, which has been set to **386.1**.

.. tabs::

   .. tab:: Tcl

      .. code:: tcl

         set g 386.1
         timeSeries Path 3 -filePath elCentro.dat -dt 0.02 -factor $g
         pattern UniformExcitation  2 1 -accel 3


   .. tab:: Python

      .. code:: python

         g = 386.1
         model.timeSeries("Path", 3, dt=0.005, filePath="A10000.dat", factor=g)
         model.pattern("UniformExcitation", 2, 1, accel=3)



Code Developed by: |fmk|
