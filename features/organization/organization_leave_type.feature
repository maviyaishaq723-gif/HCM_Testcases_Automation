@organization_module @leavetype_tests
Feature: Organization Setup - Leave Type Creation

  Scenario: Verify the creation of a new leave type record (TC_006)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Leave Type tab
    And User clicks on Add New Leave Type button
    And User fills the leave type form with valid data and clicks Create
    Then The new leave type should be created and displayed in the leave type list successfully