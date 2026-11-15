"""Deprecated: use codapact-ynab (https://pypi.org/project/codapact-ynab/)."""

from __future__ import annotations

import sys
import warnings
from pathlib import Path

# The console script prints its own notice; warn library importers only.
if Path(sys.argv[0] if sys.argv else "").stem != "ynab-api-cli":
    warnings.warn(
        "ynab-api-cli is deprecated; switch to codapact-ynab "
        "(import codapact_ynab, command `ynab`): https://pypi.org/project/codapact-ynab/",
        DeprecationWarning,
        stacklevel=2,
    )
