Dropped Capabilities
^^^^^^^^^^^^^^^^^^^^

* All commands related to reliability analysis are dropped. This however does not include the commands for sensitivity analysis.
* There are no plan to include the recently added ``damping`` commands.
* The ``mesh`` command of OpenSeesPy has been replaced by ``Model.surface``. Motivation: ``mesh`` is unpredictable, questionably defined, and needlessly cumbersome.