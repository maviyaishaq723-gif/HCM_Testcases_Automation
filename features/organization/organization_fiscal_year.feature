@organization_module @fiscalyear_tests
Feature: Organization Setup - Fiscal Year Creation

  Scenario: Verify the creation of a new fiscal year record (TC_023)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Fiscal Year tab
    And User clicks on Add New Fiscal Year button
    And User fills the fiscal year form with valid data and clicks Create
    Then The new fiscal year should be created and displayed in the fiscal year list successfully