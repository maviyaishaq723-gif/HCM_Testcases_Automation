@organization_module @performancetype_tests
Feature: Organization Setup - Performance Type Creation

  Scenario: Verify the creation of a new performance type record (TC_018)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Performance Type tab
    And User clicks on Add New Performance Type button
    And User fills the performance type form with valid data and clicks Create
    Then The new performance type should be created and displayed in the performance type list successfully