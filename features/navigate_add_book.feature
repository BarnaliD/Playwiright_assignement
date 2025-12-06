Feature: Navigate to Add New Book
  As a user
  I want to navigate from the catalog to the add-book page
  So that I can add a new book

  Scenario: User navigates to add book page
    Given User navigates to the application
    When User clicks on the add book button
    Then User should be on the add book page