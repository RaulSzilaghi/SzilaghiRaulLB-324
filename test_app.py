import pytest
from app import app, entries


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_entry_with_happiness(client):
    response = client.post(
        "/add_entry", data={"content": "Test Entry Content", "happiness": ""}
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"
    assert entry.happiness == "😃"
