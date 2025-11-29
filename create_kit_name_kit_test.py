import data
import sender_stand_request

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token() )
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test1_crear_un_kit_con_1_letra():
    new_kit_body = get_kit_body("A")
    positive_assert(new_kit_body)

def test_kit_name_511_chars():
    new_kit_body = get_kit_body("a" * 511)
    positive_assert(new_kit_body)


def test_kit_name_zero_chars():
    new_kit_body = get_kit_body("")
    negative_assert(new_kit_body)


def test_kit_name_512_chars():
    new_kit_body = get_kit_body("a" * 512)
    negative_assert(new_kit_body)


def test_kit_name_special_chars():
    new_kit_body =  get_kit_body("\"№%@\",")
    positive_assert(new_kit_body)


def test_kit_name_spaces():
    new_kit_body = get_kit_body(" A Aaa ")
    positive_assert(new_kit_body)


def test_kit_name_numbers():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)


def test_kit_name_no_parameter():
    new_kit_body = {}
    negative_assert(new_kit_body)


def test_kit_name_number_type():
    new_kit_body =  get_kit_body(123)
    negative_assert(new_kit_body)
