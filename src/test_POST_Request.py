import requests
import pytest
import allure


@allure.title("Create Booking Positive")
@allure.description("POST Request")
@allure.testcase("TC_01")
@pytest.mark.crud
def test_create_booking_positive_TC01():
    base_url = 'https://restful-booker.herokuapp.com'
    base_path = '/booking'
    url = base_url + base_path
    # we have to add headers in dictionary format
    headers = {"Content_Type": "application/JSON"}
    # Payload should also be in a normal dictionary format
    payload = {"firstname": "Jim",
               "lastname": "Brown",
               "totalprice": 111,
               "depositpaid": True,
               "bookingdates": {
                   "checkin": "2018-01-01",
                   "checkout": "2019-01-01"
               },
               "additionalneeds": "Breakfast"
               }
    response_data = requests.post(url=url, headers=headers, json=payload)
    assert response_data.status_code == 200

    json_response = response_data.json()

    booking_id = json_response["bookingid"]
    assert booking_id > 0
    assert type(booking_id) == int

    first_name = json_response["booking"]["firstname"]
    last_name = json_response["booking"]["lastname"]
    total_price = json_response["booking"]["totalprice"]
    deposit_paid = json_response["booking"]["depositpaid"]

    assert first_name == "Jim"
    assert last_name == "Brown"
    assert total_price == 111
    assert deposit_paid == True

    check_out_date = json_response["booking"]["bookingdates"]["checkout"]

    assert check_out_date == "2019-01-01"


