#!/usr/bin/env python
"""

Regular, unmodified Provider node, running with DEBUG loglevel

"""

import sys
from scripts.node_integration_tests import params

from everaapp import start

sys.argv.extend(params.PROVIDER_ARGS_NO_CONCENT)

start()
