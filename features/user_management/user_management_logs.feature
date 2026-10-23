@user_management_module @user_logs_tests
Feature: User Management - Manage User Logs History

  @TC_04
  Scenario: Verify functionality of manage user log history button (TC_04)
    Given User is logged into HCM application with valid credentials
    When User opens the Users page
    And User clicks on the Manage User Logs History button
    Then The Manage User Logs History page should be opened

  @TC_05
  Scenario: Verify filter functionality in Manage log history page (TC_05)
    Given User is logged into HCM application with valid credentials
    And User is on the Manage User Logs History page
    When User selects the current month and an employee and clicks search
    Then The filter should be applied and the logs table should be displayed

  @TC_06
  Scenario: Verify Reset button functionality (TC_06)
    Given User is logged into HCM application with valid credentials
    And User is on the Manage User Logs History page
    When User applies the filter and clicks the reset button
    Then The filter should be reset to default

  @TC_07
  Scenario: Verify search bar functionality in user logs (TC_07)
    Given User is logged into HCM application with valid credentials
    And User is on the Manage User Logs History page
    When User searches an existing user name in the logs search bar
    Then Only the logs matching that user name should be displayed

  @TC_08
  Scenario: Verify view log button functionality (TC_08)
    Given User is logged into HCM application with valid credentials
    And User is on the Manage User Logs History page
    When User clicks the view button of the first log
    Then The log details popup should be displayed

   @TC_09
  Scenario: Verify delete log button functionality (TC_09)
    Given User is logged into HCM application with valid credentials
    And User is on the Manage User Logs History page
    When User clicks the delete button of the first log and confirms with Yes
    Then That log should be deleted successfully