@employee_module @details_view
Feature: Employee Details View

  @emp_details_view
  Scenario: Verify clicking on Employee ID shows detailed employee info
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User clicks on an employee ID from the list
    Then Employee details page should open with detailed information