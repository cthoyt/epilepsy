Epilepsy Knowledge
==================
Mechanistic pathway knowledge on Epilepsy encoded in Biological Expression Language.

Installation
------------
To install the ``neurommsig_epilepsy_knowledge`` python package for programmatic access to the BEL files
in this repository, use the following code in your shell:

.. code-block:: sh

    $ git clone https://github.com/neurommsig-epilepsy/neurommsig_epilepsy.git
    $ cd neurommsig_epilepsy
    $ pip install -e .

To optionally re-compile all of the BEL files, use

.. code-block:: sh

    $ neurommsig-epilepsy-knowledge compile

Usage
-----
To get the knowledge and summarize it, use:

.. code-block:: python

    import neurommsig_epilepsy_knowledge

    graph = neurommsig_epilepsy_knowledge.repository.get_graph()
    graph.summarize()
