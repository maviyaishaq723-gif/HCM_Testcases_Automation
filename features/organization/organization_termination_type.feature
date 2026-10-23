@organization_module @terminationtype_tests
Feature: Organization Setup - Termination Type Creation

  Scenario: Verify the creation of a new termination type record (TC_015)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Termination Type tab
    And User clicks on Add New Termination Type button
    And User fills the termination type form with valid data and clicks Create
    Then The new termination type should be created and displayed in the termination type list successfully