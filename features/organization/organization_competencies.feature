@organization_module @competencies_tests
Feature: Organization Setup - Competencies Creation

  Scenario: Verify the creation of a new competencies record (TC_019)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Competencies tab
    And User clicks on Add New Competencies button
    And User fills the competencies form with name and selects type from dropdown and clicks Create
    Then The new competencies should be created and displayed in the competencies list successfully