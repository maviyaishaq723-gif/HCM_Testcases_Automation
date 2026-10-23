@organization_module @awardtype_tests
Feature: Organization Setup - Award Type Creation

  Scenario: Verify the creation of a new award type record (TC_014)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Award Type tab
    And User clicks on Add New Award Type button
    And User fills the award type form with valid data and clicks Create
    Then The new award type should be created and displayed in the award type list successfully