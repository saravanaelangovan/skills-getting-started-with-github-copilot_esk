import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide an isolated TestClient with reset in-memory state per test."""
    # Arrange: capture baseline activity state for this test.
    baseline_activities = copy.deepcopy(activities)

    # Act: provide the client to the test.
    with TestClient(app) as test_client:
        yield test_client

    # Assert/cleanup: restore original in-memory state after test.
    activities.clear()
    activities.update(baseline_activities)
