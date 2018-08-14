"""
HappyBase, a developer-friendly Python library to interact with Apache
HBase.
"""

import pkg_resources as _pkg_resources

from ._version import __version__  # noqa

from .connection import DEFAULT_HOST, DEFAULT_PORT, Connection  # noqa
from .table import Table  # noqa
from .batch import Batch  # noqa
from .pool import ConnectionPool, NoConnectionsAvailable  # noqa
