@messenger_module @messenger_tests
Feature: Messenger View and Send Message Functionality

  Scenario: Verify view message and send message button functionality
    Given User is logged into HCM application with valid credentials
    When User clicks on the header message icon and clicks View All
    Then The Messenger page should open successfully
    When User selects a chat from the messenger list
    And User types an automated test message and clicks send
    Then The message should be sent successfully in the chat