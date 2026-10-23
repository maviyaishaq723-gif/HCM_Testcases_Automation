@organization_module @dept_tests
Feature: Organization Setup - Department and Sub Department Creation

  Scenario: Verify the creation of a new department record (TC_003)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Department tab
    And User clicks on Add New Department button
    And User fills the department form with valid data and clicks Create
    Then The new department should be created and displayed in the department list successfully

  Scenario: Verify the creation of a new sub department record (TC_004)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Sub Department tab
    And User clicks on Add New Sub Department button
    And User fills the sub department form with valid data and clicks Create
    Then The new sub department should be created and displayed in the sub department list successfully