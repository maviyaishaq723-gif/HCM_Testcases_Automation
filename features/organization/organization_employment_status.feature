@organization_module @employmentstatus_tests
Feature: Organization Setup - Employment Status Creation

  Scenario: Verify the creation of a new employment status record (TC_021)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Employment Status tab
    And User clicks on Add New Employment Status button
    And User fills the employment status form with valid data and clicks Create
    Then The new employment status should be created and displayed in the employment status list successfully