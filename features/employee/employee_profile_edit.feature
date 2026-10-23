@employee_module @employee_profile_edit
Feature: Employee Profile Editing Navigation

  Scenario: Verify editing employee profile from details view
    Given User is logged into HCM application with valid credentials
    When User navigates to the Employee module
    And User clicks on an employee ID from the list
    And User clicks on Edit Profile button from profile view
    And User updates details and clicks Update button
    Then The employee profile details should be updated successfully from profile