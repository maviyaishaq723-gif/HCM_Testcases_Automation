@organization_module @goaltype_tests
Feature: Organization Setup - Goal Type Creation

  Scenario: Verify the creation of a new goal type record (TC_012)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Goal Type tab
    And User clicks on Add New Goal Type button
    And User fills the goal type form with valid data and clicks Create
    Then The new goal type should be created and displayed in the goal type list successfully