@employee_module @create
Feature: Employee Create Management

  @emp_create
  Scenario: Verify create new employee functionality with valid details
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User fills out the create new employee form with unique details
    Then A new employee should be created successfully