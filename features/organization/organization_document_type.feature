@organization_module @documenttype_tests
Feature: Organization Setup - Document Type Creation

  @TC_007
  Scenario: Verify the creation of a new document type record (TC_007)
    Given User is logged into HCM application with valid credentials
    When User opens the Document Type page under Organization Setup
    And User clicks on Create New Document Type button
    And User fills the document type form with valid data and clicks Create
    Then The new document type should be created and displayed in the document type list successfully