@organization_module @desig_tests
Feature: Organization Setup - Designation Creation

  Scenario: Verify the creation of a new designation record (TC_005)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Designation tab
    And User clicks on Add New Designation button
    And User fills the designation form with valid data and clicks Create
    Then The new designation should be created and displayed in the designation list successfully