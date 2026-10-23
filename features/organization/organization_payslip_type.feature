@organization_module @paysliptype_tests
Feature: Organization Setup - Payslip Type Creation

  Scenario: Verify the creation of a new payslip type record (TC_008)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Payslip Type tab
    And User clicks on Add New Payslip Type button
    And User fills the payslip type form with valid data and clicks Create
    Then The new payslip type should be created and displayed in the payslip type list successfully