Feature: Meeting Module Management in HCM Portal

  Background:
    Given User is logged into HCM application with valid credentials

  Scenario: Create a new meeting successfully
    When User navigates to the Meeting module
    And User creates a new meeting with required details
    Then Meeting should be successfully created

  Scenario: Edit an existing meeting successfully
    When User navigates to the Meeting module
    And User edits the first meeting from the list
    Then Meeting should be successfully edited

  Scenario: Delete an existing meeting successfully
    When User navigates to the Meeting module
    And User deletes the first meeting from the list
    Then Meeting should be successfully deleted