@employee_module @joining_letter
Feature: Employee Joining Letter

  @emp_joining_letter
  Scenario: Verify generating joining letter
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User clicks on an employee ID from the list
    And User clicks on Joining Letter and selects PDF
    Then The joining letter should be generated and displayed in a new tab