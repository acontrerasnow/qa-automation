Feature: login
  Background: login
    Given load the url /ingreso

  Scenario Outline: Login using Email and Password incorrectly
    When fill in the field by css "[name='user_email']" with value "<Email>"
    When fill in the field by css "[name="user_password"]" with value "<Password>"
    When click button with id "login-button"
    Then wait: "5" seconds until the url changes to new url
    When the user will see a message "El usuario o contraseña no son válidos." in the css "#signon-form > div.response.text-danger.mb-2"
    # Then should redirect to /mi-cuenta
    # When click "[data-autofocus="true"]"

    Examples: DATA
      | Email                           | Password     |
      | cristian_jair098@hotmail.com    | Cristian123@ |