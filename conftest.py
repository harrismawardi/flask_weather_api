import pytest
import app


@pytest.fixture
def api():
    return app.app.test_client()