@employee_module @edit
Feature: Employee Edit Management

  @emp_edit
  Scenario: Verify employee details can be edited
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User clicks the edit button for a test employee
    And User updates the employee details and saves
    Then The employee details should be updated successfully