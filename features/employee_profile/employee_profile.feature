@employee_profile_module @employee_profile_tests
Feature: User Management - Employee Profile

  @TC_15
  Scenario: Ensure the Manage employee page opens when clicked on employee id (TC_15)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    Then The Manage Employee page of that employee should be displayed

  @TC_16
  Scenario: Verify filter functionality in employee profile page (TC_16)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User opens the filter panel with the funnel icon
    And User selects branch, department and designation and clicks search on the profile filter
    Then Only the employees matching the profile filter should be displayed

  @TC_17
  Scenario: Verify edit employee profile functionality (TC_17)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    And User clicks the Edit Profile button on the Manage Employee page
    And User changes the address on the employee form and clicks Update
    Then The employee changes should be saved

  @TC_20
  Scenario: Verify edit profile button functionality in Manage employee page (TC_20)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    And User clicks the Edit Profile button on the Manage Employee page
    And User changes the address on the employee form and clicks Update
    Then The employee changes should be saved

  @TC_21
  Scenario: Verify language button functionality in Manage employee page (TC_21)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    And User selects the Chinese language
    Then The application content should be updated to Chinese

  @TC_22
  Scenario: Verify chat button functionality in manage employee page (TC_22)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    And User clicks the chat button in the header
    Then The Messenger should open displaying all the chats

  @TC_23
  Scenario: Verify message button functionality in manage employee page (TC_23)
    Given User is logged into HCM application with valid credentials
    When User opens the Employee Profile listing
    And User clicks the ID of the first employee
    And User clicks the message button in the header and then View all
    Then The Messenger should open displaying all the chats