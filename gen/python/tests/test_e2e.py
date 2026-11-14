"""End-to-end tests for this generated client. Do not edit; regenerate instead.

Offline cases always run. Live cases call the API: set YNAB_E2E_LIVE=1 (and
any credentials it needs), or point YNAB_BASE_URL at a test server.

    uv run pytest                       # offline
    YNAB_E2E_LIVE=1 uv run pytest   # offline + live
"""

from pathlib import Path

import pytest

from codapact.runtime.selftest import Skip, Suite

SUITE = Suite.load(Path(__file__).with_name("e2e.json"))


@pytest.mark.parametrize("case", SUITE.offline_cases(), ids=lambda c: c.id)
def test_offline(case, tmp_path):
    try:
        SUITE.run(case, tmp_path)
    except Skip as skip:
        pytest.skip(str(skip))


@pytest.mark.parametrize("case", SUITE.live_cases(), ids=lambda c: c.id)
def test_live(case, tmp_path):
    try:
        SUITE.run(case, tmp_path)
    except Skip as skip:
        pytest.skip(str(skip))
