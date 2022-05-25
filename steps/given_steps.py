from selenium import webdriver
from behave import given
import routes


@given("load the url {path}")
def step_load_page(context, path):
    base_url = routes.route.url_base
    context.driver = webdriver.Chrome('drivers/chromedriver.exe')
    context.driver.get(base_url + path)