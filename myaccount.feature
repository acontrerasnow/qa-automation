Feature: login
  Background: login
    Given load the url /my-account

  Scenario Outline: Login using Email and Password incorrectly
    When fill in the field by css "[name='identifier']" with value "<Phone>"
    When fill in the field by css "[name="password"]" with value "<Password>"
    When click button with class name "_26w467ijGHqiyBCen3Gyoh"
    Then wait: "5" seconds until the url changes to new url
    When the user will see a message "Username doesn't exist" in the css "._1on8LaEFyhjLwx0A2VukLC"
    # Then should redirect to /mi-cuenta
    # When click "[data-autofocus="true"]"

    Examples: DATA
      | Phone                           | Password     |
      | 123456789                       | 1293skd |

  Scenario Outline: Login using Phone and Password correctly
    When fill in the field by css "[name='identifier']" with value "<Phone>"
    When fill in the field by css "[name="password"]" with value "<Password>"
    When click button with class name "_26w467ijGHqiyBCen3Gyoh"
    Then wait: "5" seconds until the url changes to new url
    #When the user will see a message "Username doesn't exist" in the css "._1on8LaEFyhjLwx0A2VukLC"
    # Then should redirect to /mi-cuenta
    # When click "[data-autofocus="true"]"

    Examples: DATA
      | Phone                            | Password     |
      | 9997554866                       | Testing1234 |