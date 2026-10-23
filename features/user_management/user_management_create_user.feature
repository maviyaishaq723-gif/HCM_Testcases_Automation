@user_management_module @user_tests
Feature: User Management - New User Creation

  Scenario: Verify the creation of a new user record (TC_03)
    Given User is logged into HCM application with valid credentials
    When User navigates to the User Management section
    And User clicks on the User tab
    And User clicks on Add New User button
    And User fills the user form with valid data and selects role and clicks Create
    Then The new user should be created and displayed in the user list successfully