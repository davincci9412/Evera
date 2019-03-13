#!/usr/bin/env python
"""

Requestor Node that doesn't send `AckReportComputedTask` in response to
Provider's `ReportComputedTask` message, thus triggering the Provider to
reach out to the Concent.

"""

import mock
import sys

from evera_messages.message import RandVal
from scripts.node_integration_tests import params

from everaapp import start  # noqa: E402 module level import not at top of file

sys.argv.extend(params.REQUESTOR_ARGS_DEBUG)

with mock.patch(
        "evera.task.tasksession.concent_helpers.process_report_computed_task",
        mock.Mock(return_value=RandVal())):
    start()
