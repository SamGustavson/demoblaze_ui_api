import requests
import base64
import uuid

USERNAME = "test"
PASSWORD = "test"
EXPECTED_PRODUCT_TITLE = "Nexus 6"
ITEMS = "Items"
PROD_ID = "prod_id"
DEMO_BLAZE_BASE_URL = "https://api.demoblaze.com"

INDEX = 0
EXPECTED_ITEMS_COUNT = 1
EXPECTED_PRODUCT_NEXUS6_ID = 3
EXPECTED_PRODUCT_NEXUS6_PRICE = 650
EXPECTED_STATUS_CODE_OK = 200


def verify_product_param_api():
    verify_product(verify_items_count_and_get_product_id(get_user_cookie_via_login()))


def get_user_cookie_via_login():
    login_response = login()
    return get_user_cookie(login_response)


def verify_items_count_and_get_product_id(user_cookie):
    view_cart_response = get_list_of_items(user_cookie).json()

    if len(view_cart_response[ITEMS]) == 0:
        add_product_to_cart(user_cookie)
        view_cart_response = get_list_of_items(user_cookie).json()
        verify_view_cart_response(view_cart_response, INDEX)
    else:
        verify_view_cart_response(view_cart_response, INDEX)

    return get_prod_id(view_cart_response, INDEX)


def verify_product(product_id):
    view_response = get_product_data(product_id).json()

    verify_product_id_after_view_api(view_response, product_id)
    verify_product_title(view_response, EXPECTED_PRODUCT_TITLE)
    verify_product_price(view_response, EXPECTED_PRODUCT_NEXUS6_PRICE)
    print("Success, Product verified")


def login():
    user_login_details = {"username": USERNAME, "password": get_password_base64().decode()}
    login_response = requests.post(f"{DEMO_BLAZE_BASE_URL}/login", json=user_login_details)
    assert login_response.status_code == EXPECTED_STATUS_CODE_OK
    return login_response


def get_password_base64():
    password = PASSWORD
    return base64.b64encode(password.encode('ascii'))


def get_user_cookie(login_response):
    return login_response.content.decode().replace('\"\n', "").split(": ")[1]


def get_list_of_items(user_cookie):
    user_credentials_data = {"cookie": user_cookie, "flag": True}
    view_cart_response = requests.post(f"{DEMO_BLAZE_BASE_URL}/viewcart", json=user_credentials_data)
    assert view_cart_response.status_code == EXPECTED_STATUS_CODE_OK
    return view_cart_response


def add_product_to_cart(user_cookie):
    add_product_data = {"cookie": user_cookie, "flag": True, "id": str(uuid.uuid4()), PROD_ID: EXPECTED_PRODUCT_NEXUS6_ID}
    add_to_cart_response = requests.post(f"{DEMO_BLAZE_BASE_URL}/addtocart", json=add_product_data)
    assert add_to_cart_response.status_code == EXPECTED_STATUS_CODE_OK


def get_prod_id(view_cart_response_json_body, item_index):
    return view_cart_response_json_body[ITEMS][item_index][PROD_ID]


def get_product_data(product_id):
    product_data = {"id": product_id}
    view_response = requests.post(f"{DEMO_BLAZE_BASE_URL}/view", json=product_data)
    assert view_response.status_code == EXPECTED_STATUS_CODE_OK
    return view_response


def verify_view_cart_response(view_cart_response, item_index):
    verify_items_count(view_cart_response, EXPECTED_ITEMS_COUNT)
    verify_product_id_after_view_cart_api(view_cart_response, item_index, EXPECTED_PRODUCT_NEXUS6_ID)


def verify_items_count(view_cart_response, expected_count):
    assert len(view_cart_response) == expected_count


def verify_product_id_after_view_cart_api(view_cart_response, item_index, expected_product_id):
    assert view_cart_response[ITEMS][item_index][PROD_ID] == expected_product_id


def verify_product_id_after_view_api(view_response_json_body, expected_product_id):
    assert view_response_json_body["id"] == expected_product_id


def verify_product_title(view_response, expected_title):
    assert view_response["title"] == expected_title


def verify_product_price(view_response, expected_price):
    assert view_response["price"] == expected_price