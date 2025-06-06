BandGeneral
^^^^^^^^^^^

This command is used to construct a BandGeneral linear system of equation. 
This class is used for matrix systems which have a banded profile. 
The matrix is stored as shown below in a 1-dimensional array of size equal to the bandwidth times the number of unknowns. 
When a solution is required, the `Lapack <https://en.wikipedia.org/wiki/LAPACK>`__ routines *DGBSV* and *SGBTRS* are used. 

.. tabs::
   .. tab:: Python

      .. py:method:: Model.system("BandGeneral")
         :no-index:

         Configure the system to use the BandGeneral solver.

   .. tab:: Tcl

      .. function:: system BandGeneral

         Configure the system to use the BandGeneral solver.


An :math:`n \times n` matrix A=(ai,j) is a band matrix if all matrix elements are zero outside a diagonally bordered band whose range is determined by constants :math:`k_1` and :math:`k_2`:

.. math::
   
   A_{ij}=0 \quad \mbox{if}\quad j<i-k_1 \quad\mbox{ or }\quad j>i+k_2; \quad k_1, k_2 \ge 0.

The quantities :math:`k_1` and :math:`k_2` are the left and right half-bandwidth, respectively. 
The bandwidth of the matrix is :math:`k_1 + k_2 + 1` and only the entries in the band are stored; the rest being implicitly zero.

For example, 6-by-6 a matrix with bandwidth 3:

.. math::

   \begin{bmatrix}
   B_{11} & B_{12} & 0 & \cdots & \cdots & 0 \\
   B_{21} & B_{22} & B_{23} & \ddots & \ddots & \vdots \\
    0     & B_{32} & B_{33} & B_{34} & \ddots & \vdots \\
    \vdots & \ddots & B_{43} & B_{44} & B_{45} & 0 \\
    \vdots & \ddots & \ddots & B_{54} & B_{55} & B_{56} \\
    0      & \cdots & \cdots & 0      & B_{65} & B_{66}
    \end{bmatrix}


is stored as the 6-by-3 matrix

.. math::

   \begin{bmatrix}
   0 & B_{11} & B_{12}\\
   B_{21} & B_{22} & B_{23} \\
   B_{32} & B_{33} & B_{34} \\
   B_{43} & B_{44} & B_{45} \\
   B_{54} & B_{55} & B_{56} \\
   B_{65} & B_{66} & 0
   \end{bmatrix}

Example 
-------

The following example shows how to construct a *BandGeneral* system

1. **Tcl Code**

   .. code-block:: tcl

      system BandGeneral

2. **Python Code**

   .. code-block:: python

      model.system('BandGeneral')

Code Developed by: |fmk|

