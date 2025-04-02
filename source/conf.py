#!/usr/bin/env python3
import os
import sys
from pathlib import Path
# import sphinx_rtd_theme
#sys.path.append(os.path.abspath('./sphinx_ext/'))

#
# -- Project information -----------------------------------------------------
#
project = "xara"
copyright = 'Berkeley, CA'
description = "Finite element analysis"
author = "PEER"
#html_logo = "_static/images/xara.png"
html_title = "xara: Nonlinear finite element analysis" # "xara: An OpenSees application"
html_short_title = "xara"

root_doc = "launch" #"user/index"
html_additional_pages = {'index': 'home.html'}
html_extra_path = ["robots.txt"]

rst_prolog = """
.. |floatList| replace:: *list float*
.. |integerList| replace:: *list integer*
.. |integerTuple| replace:: *tuple integer*
.. |intList| replace:: *list integer*
.. |listFloat| replace:: *list float*
.. |listInteger| replace:: *list integer*
.. |listInt| replace:: *list integer*
.. |floatTuple| replace:: *tuple of float*
.. |list| replace:: *list*
.. |kwds| replace:: `kwds <kwds>`__
.. |bool| replace:: *bool*
.. |string| replace:: *string*
.. |str|  replace:: *str*
.. |float| replace:: *float*
.. |integer| replace:: *integer*
.. |OPS| replace:: xara
.. |BRACE2| replace:: `BRACE2`_
.. _BRACE2: https://structures.live
.. |OpenSeesRT| replace:: `OpenSeesRT`_
.. _OpenSeesRT: https://stairlab.berkeley.edu/software/opensees/
.. |OpenSees| replace:: OpenSees
.. |OPS link| replace:: `OpenSees app`_
.. _OpenSees app: https://stairlab.berkeley.edu/software/OpenSeesRT/
.. |githubLink| replace:: `OpenSees Github link`_
.. _OpenSees Github link: https://github.com/STAIRLab/OpenSeesRT
.. |messageBoard| replace:: `OpenSees Message Board`_
.. _OpenSees Message Board: https://github.com/claudioperez/OpenSeesRT/discussions
.. |glf| replace:: `Gregory L. Fenves`_
.. _Gregory L. Fenves: http://www.caee.utexas.edu/faculty/directory/fenves
.. only:: html

   .. |mhs| raw:: html

      <a href="https://web.engr.oregonstate.edu/~mhscott/" rel="nofollow">Michael H. Scott</a>
..
    .. only:: not html

       .. |mhs| replace:: `Michael H. Scott`_
       .. _Michael H. Scott: https://cce.oregonstate.edu/scott

.. |fmk| replace:: *fmk*
.. |fcf| replace:: `fcf`_
.. _fcf: https://fedeas.net
.. |rms| replace:: *Remo Magalhaes de Souza*
.. |cmp| replace:: `Claudio M. Perez`_
.. _Claudio M. Perez: https://stairlab.berkeley.edu/people/claudioperez
.. |pedro| replace:: `Pedro Arduino`_
.. _Pedro Arduino: https://www.ce.washington.edu/facultyfinder/pedro-arduino
.. |peter| replace:: `Peter Mackenzie-Helnwein`_
.. _Peter Mackenzie-Helnwein: https://www.ce.washington.edu/facultyfinder/peter-mackenzie-helnwein
.. |chris| replace:: `Chris McGann`_
.. _Chris McGann: https://www.canterbury.ac.nz/engineering/contact-us/people/chris-mcgann.html
.. |andreas| replace:: *Andreas Schellenberg*
.. |csasj| replace:: *csasj*

"""

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#   'toctree_filter',
#   'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    "sphinx.ext.autosummary",
    'sphinxcontrib.bibtex',
    'sphinx_sitemap'
]

bibtex_bibfiles = ["references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['_static']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "**/hidden",
    "user/index.rst",
    "user/manual/model/geomTransf/frame/index.rst",
    "user/manual/analysis/integrator/gimmeMCK.rst",
    "user/manual/analysis/modalProperties.rst",
    "user/manual/analysis/responseSpectrumAnalysis.rst",
    "user/manual/model/damping/elementalDamping.rst",
    "user/manual/model/eleLoad.rst",
    "user/manual/model/elements/ASDEmbeddedNodeElement.rst",
    "user/manual/model/elements/FourNodeTetrahedron.rst",
    "user/manual/model/elements/frame/PointFrame.rst",
    "user/manual/model/elements/other/InertiaTruss.rst",
    "user/manual/model/elements/other/MEFI.rst",
    "user/manual/model/elements/other/ModElasticBeam.rst",
    "user/manual/model/elements/other/gradientInelasticBeamColumn.rst",
    "user/manual/model/elements/other/MVLEM_3D.rst",
    "user/manual/model/elements/other/SFI_MVLEM_3D.rst",
    "user/manual/model/elements/other/E_SFI.rst",
    "user/manual/model/elements/other/E_SFI_MVLEM_3D.rst",
    "user/manual/model/elements/fluid/7045-BbarBrickUP.rst",
    "user/manual/model/elements/fluid/7046-BbarQuadUP.rst",
    "user/manual/model/elements/fluid/7066-BrickUP.rst",
    "user/manual/model/elements/fluid/7264-FourNodeQuadUP.rst",
    "user/manual/model/elements/fluid/7266-Four Node QuadUP.rst",
    "user/manual/model/elements/fluid/7419-NineFourNodeQuadUP.rst",
    "user/manual/model/elements/fluid/7612-SSPbrickUP.rst",
    "user/manual/model/elements/fluid/7614-SSPquadUP.rst",
    "user/manual/model/elements/fluid/7720-TwentyEightNodeBrickUP.rst",
    "user/manual/model/elements/fluid/index.rst",
    "user/manual/materialCommands.rst",
    "user/manual/material/ndMaterials/BoundingCamClay.rst",
    "user/manual/material/ndMaterials/PM4Sand.rst",
    "user/manual/material/ndMaterials/PM4Silt.rst",
    "user/manual/material/ndMaterials/PressureIndependentMultiYield.rst",
    "user/manual/material/ndMaterials/PressureIndependentMultiYieldExample1.rst",
    "user/manual/material/ndMaterials/PressureDependentMultiYield.rst",
    "user/manual/material/ndMaterials/PressureDependentMultiYield02.rst",
    "user/manual/material/ndMaterials/J2CyclicBoundingSurface.rst",
    "user/manual/material/ndMaterials/SAniSandMS.rst",
    "user/manual/material/ndMaterials/Orthotropic.rst",
    "user/manual/material/ndMaterials/Series3D.rst",
    "user/manual/material/ndMaterials/Parallel3D.rst",
    "user/manual/material/ndMaterials/InitStrain.rst",
    "user/manual/material/ndMaterials/ASDConcrete3D.rst",
    "user/manual/material/ndMaterials/ASDPlasticMaterial/*",
    "user/manual/material/ndMaterials/ASDPlasticMaterial.rst",
    "user/manual/material/ndMaterials/OrthotropicRAConcrete.rst",
    "user/manual/material/ndMaterials/SmearedSteelDoubleLayer.rst",
    "user/manual/section/ASDCoupledHinge3D.rst",
    "user/manual/section/LayeredMembraneSection.rst",
    "user/manual/section/ReinforcedConcreteLayeredMembraneSection.rst",
    "user/manual/output/getCrdTransfTags.rst",

    "user/manual/model/nodes/sp.rst",
    "user/examples/basicExamples/basicTruss.rst",
    "user/manual/material/matTestCommands.rst",
#   "user/manual/model/beamIntegration.rst",
#   "user/manual/model/beamIntegrations/test.rst",
#   "user/manual/model/beamIntegrations/CompositeSimpson.rst",
#   "user/manual/model/beamIntegrations/ConcentratedCurvature.rst",
#   "user/manual/model/beamIntegrations/ConcentratedPlasticity.rst",
#   "user/manual/model/beamIntegrations/FixedLocation.rst",
#   "user/manual/model/beamIntegrations/HingeEndpoint.rst",
#   "user/manual/model/beamIntegrations/HingeMidpoint.rst",
#   "user/manual/model/beamIntegrations/HingeRadau.rst",
#   "user/manual/model/beamIntegrations/HingeRadauTwo.rst",
#   "user/manual/model/beamIntegrations/Legendre.rst",
#   "user/manual/model/beamIntegrations/Lobatto.rst",
#   "user/manual/model/beamIntegrations/LowOrder.rst",
#   "user/manual/model/beamIntegrations/MidDistance.rst",
#   "user/manual/model/beamIntegrations/NewtonCotes.rst",
#   "user/manual/model/beamIntegrations/Radau.rst",
#   "user/manual/model/beamIntegrations/Trapezoidal.rst",
#   "user/manual/model/beamIntegrations/UserHinge.rst",
#   "user/manual/model/beamIntegrations/userDefined.rst",
    "user/manual/model/damping/elementalDamping/SecStifDamping.rst",
    "user/manual/model/damping/elementalDamping/URDDamping.rst",
    "user/manual/model/damping/elementalDamping/UniformDamping.rst",

    "user/manual/model/timeseries/MPAccTimeSeries.rst",
    "user/manual/model/timeseries/PeerNGAMotion.rst",
    "user/manual/model/timeseries/RampTimeSeries.rst",
    "user/manual/model/timeseries/peerMotion.rst",
    "user/manual/model/timeseries/pulseTimeSeries.rst",
    "user/manual/model/timeseries/rectangularTimeSeries.rst",
    "user/manual/model/timeseries/triangleTimeSeries.rst",
    "user/manual/model/timeseries/trigTimeSeries.rst",
]

# -- Options for HTML output -------------------------------------------------

html_baseurl       = "https://opensees.stairlab.io/"
sitemap_url_scheme = "{link}"

html_theme = "sphinx_book_theme" #"pydata_sphinx_theme" #"sphinx_rtd_theme"
html_show_sphinx = False
html_show_sourcelink = False

if html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        'navigation_depth': 5,
        'logo_only': True,
        'style_nav_header_background': 'white',
        'prev_next_buttons_location': None,
    }
else:
    html_theme_options = {
    #   'analytics_id': 'UA-2431545-1',
    #   "body_max_width": None,
        "show_prev_next": False,
        "logo": {
#         "image_light": html_logo,
#         "image_dark": "_static/logo-dark.png",
          "link": html_baseurl, # "index.html",
          "text": f'<span class="lead display-3">{project}</span>',
#         "alt_text": "xara docs - Home",
        }
    }
if "book" in html_theme:
    html_theme_options.update({
        "use_download_button":  False,
        "use_edit_page_button": False,
        "article_header_start": ["toggle-primary-sidebar.html", "breadcrumbs"]
    })

html_context = {
    "root_doc": root_doc,
    "description": description,
    "github_user": "STAIRLab",
    "github_repo": "OpenSeesRT",
#   "doc_path": "<path-from-root-to-your-docs>",

    # HOME
    "examples": [],
    "features": [
        {"title": "Fast", "body": "Core components have been refactored to leverage modern C++ features, which has furnished substantial performance improvements over the alternative serial OpenSees interpreters."},
        {"title": "Free", "body": "All source code contributed to xara is licensed under a <em>pure</em> BSD."},
        {"title": "Robust", "body": '<em>xara</em> is designed from the ground up for use in production environments like <a href="https://structures.live">structures.live</a>'},
    ],
    "home_image": "_static/images/CableStayed02.png"
}

#  'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B,

html_css_files = [
    'css/custom.css'
] + [
    'css/home-css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/home-css/").glob("vars*.css")
] + [
     'css/css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/css/").glob("*.css")
] + [
    "css/veux.css",
]

html_secnum_suffix = " "


