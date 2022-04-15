import pytest

from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_sign_up():

    payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )

    response = client.post("/api/v1/auth/users/", payload, format="json")
    data = response.data

    # djoser does not return address and cellphone_number
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]
    assert "address" not in data
    assert "cellphone_number" not in data
    assert "password" not in data


# TODO use fictures from conftest.py
@pytest.mark.django_db
def test_log_in_user():

    #register user
    payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )
    client.post("/api/v1/auth/users/", payload, format="json")

    # log in (get auth token)
    payload = dict(
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73"
    )
    response = client.post("/api/v1/auth/token/login", payload, format="json")
    data = response.data

    assert "auth_token" in data
    assert response.status_code == 200


#todo use fixture
@pytest.mark.django_db
def test_log_in_user_fail():

    #register user
    payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )
    client.post("/api/v1/auth/users/", payload, format="json")

    # log in (get auth token)
    payload = dict(
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73xxxxx"
    )
    response = client.post("/api/v1/auth/token/login", payload, format="json")
    data = response.data

    assert "auth_token" not in data
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_user_me():

    # register user
    register_payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )
    client.post("/api/v1/auth/users/", register_payload, format="json")

    # log in (get auth token)
    payload = dict(
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73"
    )
    response = client.post("/api/v1/auth/token/login", payload, format="json")
    data = response.data
    auth_token = data["auth_token"]

    response_me = client.get("/api/v1/users/me/", HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response_me.status_code == 200

    data = response_me.data
    assert data["is_staff"] == False
    assert data["email"] == register_payload["email"]


@pytest.mark.django_db
def test_get_user_log_out():

    # register user
    register_payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )
    client.post("/api/v1/auth/users/", register_payload, format="json")

    # log in (get auth token)
    payload = dict(
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73"
    )
    response = client.post("/api/v1/auth/token/login", payload, format="json")
    data = response.data
    auth_token = data["auth_token"]

    response_me = client.post("/api/v1/auth/token/logout/", HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response_me.status_code == 204


