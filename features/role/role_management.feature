@role_module @role_tests
Feature: User Management - Role

  @TC_11
  Scenario: Verify create new role button functionality for existing role (TC_11)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Role page
    And User clicks on Create New Role button
    And User fills the role form with an already existing role name and clicks Create
    Then An error should be displayed that the role already exists

  @TC_12
  Scenario: Verify search bar functionality in role (TC_12)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Role page
    And User searches an existing role in the roles search bar
    Then Only the roles matching the searched name should be displayed