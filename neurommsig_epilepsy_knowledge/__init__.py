# -*- coding: utf-8 -*-

"""Epilepsy curation repository."""

import os

from bel_repository import BELMetadata, BELRepository
from bel_repository.utils import serialize_authors

__all__ = [
    'repository',
    'metadata',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by last name
AUTHORS = [
    'Nora Filep',
    'Anka Gueldenpfennig',
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernandez',
]

# All metadata is grouped here
metadata = BELMetadata(
    name='Epilepsy Curation',
    version=VERSION,
    authors=serialize_authors(AUTHORS),
    contact='daniel.domingo.fernandez@scai.fraunhofer.de',
    description="Mechanistic knowledge surrounding Epilepsy",
    license='CC BY 4.0',
)

repository = BELRepository(
    HERE,
    metadata=metadata,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
