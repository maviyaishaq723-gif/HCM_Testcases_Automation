@organization_module @deductionoption_tests
Feature: Organization Setup - Deduction Option Creation

  Scenario: Verify the creation of a new deduction option record (TC_011)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Deduction Option tab
    And User clicks on Add New Deduction Option button
    And User fills the deduction option form with valid data and clicks Create
    Then The new deduction option should be created and displayed in the deduction option list successfully