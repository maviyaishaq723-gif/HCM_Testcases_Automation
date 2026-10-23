@organization_module @loanoption_tests
Feature: Organization Setup - Loan Option Creation

  Scenario: Verify the creation of a new loan option record (TC_010)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Loan Option tab
    And User clicks on Add New Loan Option button
    And User fills the loan option form with valid data and clicks Create
    Then The new loan option should be created and displayed in the loan option list successfully