#!/usr/bin/env python
"""

Regular, unmodified Provider node

"""

import sys
from scripts.node_integration_tests import params

from everaapp import start  # noqa: E402 module level import not at top of file

sys.argv.extend(params.PROVIDER_ARGS)

start()
