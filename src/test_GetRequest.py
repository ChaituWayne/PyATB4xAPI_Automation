import requests
import pytest
import allure

@allure.description("Get Request")
@allure.testcase("TC_01")
@pytest.mark.regression
def test_sample_get():
    url = 'https://restful-booker.herokuapp.com/booking/735'
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 200

@allure.description("Get Request")
@allure.testcase("TC_02")
@pytest.mark.regression
def test_sample_get_negative():
    url = 'https://restful-booker.herokuapp.com/booking/-1'
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404
