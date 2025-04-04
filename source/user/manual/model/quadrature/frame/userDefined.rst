.. _UserDefined-BeamIntegration:


UserDefined
^^^^^^^^^^^

This class allows the user to specified locations and weights of the integration points.

.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.beamIntegration("UserDefined", tag, N, sections, locs, wts)
         :no-index:

         :param |integer| tag: The tag of the beam integration.
         :param |integer| N: The number of integration points along the element.
         :param |intTuple| sections: A list of previously-defined section objects.
         :param |floatTuple| locs: Locations of integration points along the element.
         :param |floatTuple| wts: Weights of integration points.

   .. tab:: Tcl 

      .. function:: beamIntegration "UserDefined" tag N secTags locs wts

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``tag``, |integer|,              tag of the beam integration
         ``N``, |integer|,             number of integration points along the element.
         ``secTags``, |integerList|,        A list previous-defined section objects.
         ``locs``, |floatList|,           Locations of integration points along the element.
         ``wts``, |floatList|,            weights of integration points.


   Places ``N`` integration points along the element, which are defined in ``locs``
   on the natural domain :math:`[0, 1]`. The weight of each integration point is
   defined in the ``wts`` also on the :math:`[0, 1]` domain.
   The force-deformation response at each integration point
   is defined by the ``secs``. The ``locs``, ``wts``, and ``secs``
   should be of length ``N``. 
   In general, there is no accuracy for this approach to numerical integration.


      
Example
-------

The following examples demonstrate the command in Tcl and Python script to add a *UserDefined* beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

.. tabs::

  .. tab:: Tcl

     .. code-block:: Tcl

        set locs  {0.1, 0.3, 0.5, 0.7, 0.9}
        set wts  {0.2, 0.15, 0.3, 0.15, 0.2}
        set secs  {1, 2, 2, 2, 1}
        beamIntegration "UserDefined" 1 5  $secs  $locs $wtsa


  .. tab:: Python

     .. code-block:: python

        locs = (0.1, 0.3 , 0.5, 0.7 , 0.9)
        wts  = (0.2, 0.15, 0.3, 0.15, 0.2)
        secs = (  1,    2,   2,    2,   1)
        model.beamIntegration("UserDefined",1, len(secs), secs, locs, wts)


