.. _modelClass:

Model
^^^^^

The ``Model`` class is an alternative to the ``model`` command in Python 
that creates an isolated model that is safe from global state corruption. 
An instance of ``Model`` has all of the standard OpenSees modeling commands 
exposed as methods.

.. The command is also used to define the spatial dimension of the subsequent nodes to be added and the number of degrees-of-freedom at each node. 

.. py:class:: Model(ndm, ndf=None, echo_file=None)

   Create an isolated model for given number of dimensions and number of DOFs.

   :param |integer| ndm: number of dimensions
   :param |integer| ndf: number of dofs (optional, default ``ndm*(ndm+1)/2``)
   :param *FileLike* echo_file: Optional file handle to write command history to.

   .. py:attribute:: ndm
      :type: int

      The number of dimensions in the model.

   .. py:attribute:: ndf
      :type: int

      The number of degrees-of-freedom at each node.

.. note:: 

   The ``Model`` class is currently only available in the experimental 
   `xara <http://pypi.org/project/xara>`_ Python package.
   To install ``xara``, just run:

   .. code-block:: bash

      pip install xara

..
   This experimental package exposes an identical interface to ``openseespy``, but must
   be imported as ``opensees.openseespy`` as opposed to ``openseespy.opensees``. 
   For more information, visit `GitHub <https://github.com/STAIRLab/OpenSeesRT>`_.


The ``Model`` class prevents inadvertent corruption of global state that may be caused when using
the ``model`` command that was implemented by older finite element interpreters.
Each instance of a ``Model`` owns a unique instance of an interpreter which can only be manipulated
through the instance itself. 
This interpreter can be be used from Python to invoke either Tcl or Python commands. 
These additional commands are described in the subsequent sections.


Example
-------

The following examples demonstrate the creation of a ``Basic`` model builder that will 
create nodes with in 2D space (``ndm`` of ``2``) and with ``ndf=3`` degrees-of-freedom at each node.


.. code-block:: Python

   import xara
   model = xara.Model(ndm=2, ndf=3)

   model.node(1, 2.0, 3.0)
   ...

For more examples, visit the STAIRlab example `gallery <https://gallery.stairlab.io>`_.

Code Developed by: |cmp|

