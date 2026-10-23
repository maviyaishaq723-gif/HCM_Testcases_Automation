@organization_module @jobsetup_tests
Feature: Organization Setup - Job Category and Job Stage Creation

  Scenario: Verify the creation of a new job category record (TC_016)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Job Category tab
    And User clicks on Add New Job Category button
    And User fills the job category form with valid data and clicks Create
    Then The new job category should be created and displayed in the job category list successfully

  Scenario: Verify the creation of a new job stage record (TC_017)
    Given User is logged into HCM application with valid credentials
    When User navigates to the Organization Setup section
    And User clicks on the Job Stage tab
    And User clicks on Add New Job Stage button
    And User fills the job stage form with valid data and clicks Create
    Then The new job stage should be created and displayed in the job stage list successfully