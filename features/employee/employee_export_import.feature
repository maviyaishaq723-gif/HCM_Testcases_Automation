@employee_module
Feature: Employee Module Management in HCM Portal

  @emp_export @smoke
  Scenario: Verify export functionality on Employee page
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User clicks on the Export Employee button
    Then An Excel file with employee data should be downloaded

  @emp_import
  Scenario: Verify import functionality on Employee page
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User uploads an employee sample document
    Then Employee file should be uploaded successfully