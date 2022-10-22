from unittest.mock import Mock

import pytest

from rele.apps import ReleConfig


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests():
    ReleConfig.ready = Mock()
