@organization_module @trainingtype_tests
Feature: Organization Setup - Training Type Creation

  Scenario: Verify the creation of a new training type record (TC_013)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Training Type tab
    And User clicks on Add New Training Type button
    And User fills the training type form with valid data and clicks Create
    Then The new training type should be created and displayed in the training type list successfully