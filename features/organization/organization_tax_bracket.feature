@organization_module @taxbracket_tests
Feature: Organization Setup - Tax Bracket Creation

  Scenario: Verify the creation of a new tax bracket record (TC_022)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Tax Bracket tab
    And User clicks on Add New Tax Bracket button
    And User fills the tax bracket form with valid data and clicks Submit
    Then The new tax bracket should be created and displayed in the tax bracket list successfully