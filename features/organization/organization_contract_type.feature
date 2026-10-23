@organization_module @contracttype_tests
Feature: Organization Setup - Contract Type Creation

  Scenario: Verify the creation of a new contract type record (TC_020)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Contract Type tab
    And User clicks on Add New Contract Type button
    And User fills the contract type form with valid data and clicks Create
    Then The new contract type should be created and displayed in the contract type list successfully