import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health"
    )

    assert response.status_code == 200, response.content
    assert response.json()["status"] == 1


def test_post_health():
    response = requests.post(
        url=f"{API_URL}/health"
    )

    assert response.status_code == 200, response.content
    assert response.json()["status"] == 1
    assert "comment" in response.json()


def test_get_object():

    object_id = 123

    response = requests.get(
        url=f"{API_URL}/objects",
        params={"object_id": object_id}
    )

    assert response.status_code == 200, response.content
    assert response.json()["object_id"] == object_id

    object_id = 1234

    response = requests.get(
        url=f"{API_URL}/objects",
        params={"object_id": object_id}
    )

    assert response.status_code == 404, response.content


def test_get_users():
    response = requests.get(
        url=f"{API_URL}/users"
    )

    assert response.status_code == 400
    
    assert response.status_code == 200, response.content
    assert response.json()["status"] == 1
    assert len(response.json()["users"]) == 2, response.json()
