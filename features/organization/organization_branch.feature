@organization_module @branch_tests
Feature: Organization Setup - Branch Creation

  Scenario: Verify the creation of a new branch record
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on Create New Branch button
    And User fills the branch form with valid data and clicks Save
    Then The new branch should be created and displayed in the branch list successfully