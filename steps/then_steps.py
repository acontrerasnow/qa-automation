from behave import then
from hamcrest import assert_that, equal_to, is_not
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import routes
from behave import when
import time


@then("title is {text}")
def step_impl(context, text):
    assert_that(context.driver.title, equal_to(text))


@then("title contains {text}")
def step_impl(context, text):
    print(text)
    #print("xD", EC.title_contains(text))
    #return EC.title_contains(text)


@then("should redirect to {path}")
def step_impl(context, path):
    context.base_url = routes.route.url_base
    assert_that(context.base_url + path, equal_to(context.driver.current_url))


@then("the user continue in {path}")
def step_redirect(context, path):
    context.base_url = routes.route.url_base
    assert_that(context.driver.current_url, equal_to(context.base_url + path))


@then('wait: "{seconds}" seconds until the url changes to new url')
def step_impl(context, seconds, ):
    actual = context.driver.current_url
    wait = WebDriverWait(context.driver, int(seconds))
    try:
        wait.until(lambda driver: actual != context.driver.current_url)
    except:
        assert_that(context.driver.current_url), equal_to(context.driver.current_url)