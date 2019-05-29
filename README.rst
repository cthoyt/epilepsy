Epilepsy Knowledge
==================
Mechanistic pathway knowledge on Epilepsy encoded in Biological Expression Language.

Installation
------------
To install the ``epilepsy_knowledge`` python package for programmatic access to the BEL files
in this repository, use the following code in your shell:

.. code-block:: sh

    $ git clone https://github.com/cthoyt/epilepsy.git
    $ epilepsy
    $ pip install -e .

To compile all of the BEL files, use

.. code-block:: sh

    $ epilepsy-knowledge compile

Usage
-----
To get the knowledge and summarize it, use:

.. code-block:: python

    import epilepsy_knowledge

    graph = epilepsy_knowledge.repository.get_graph()
    graph.summarize()
