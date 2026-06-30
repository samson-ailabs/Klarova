# SPDX-FileCopyrightText: 2026 Son Dang Dinh
# SPDX-License-Identifier: Apache-2.0
import re

import pytest

import klarova


def test_version_is_semver() -> None:
    assert isinstance(klarova.__version__, str)
    assert re.fullmatch(r"\d+\.\d+\.\d+", klarova.__version__)


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    klarova.main()
    assert "Klarova" in capsys.readouterr().out
