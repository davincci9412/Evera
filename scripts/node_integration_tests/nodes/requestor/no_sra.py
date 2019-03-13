#!/usr/bin/env python
"""

Requestor Node that doesn't send `SubtaskResultsAccepted`

"""
import mock
import sys

from evera_messages.message.tasks import SubtaskResultsAccepted
from evera.task.tasksession import TaskSession
from scripts.node_integration_tests import params

from everaapp import start  # noqa: E402 module level import not at top of file

sys.argv.extend(params.REQUESTOR_ARGS_DEBUG)

original_send = TaskSession.send


def send(self, msg, *args, **kwargs):

    # fail to send `SubtaskResultsAccepted`
    if isinstance(msg, SubtaskResultsAccepted):
        return

    original_send(self, msg, *args, **kwargs)


with mock.patch("evera.task.tasksession.TaskSession.send", send):
    start()
