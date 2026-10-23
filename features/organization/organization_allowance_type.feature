@organization_module @allowancetype_tests
Feature: Organization Setup - Allowance Type Creation

  Scenario: Verify the creation of a new allowance option record (TC_009)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Allowance Type tab
    And User clicks on Add New Allowance Type button
    And User fills the allowance type form with valid data and clicks Create
    Then The new allowance type should be created and displayed in the allowance type list successfully