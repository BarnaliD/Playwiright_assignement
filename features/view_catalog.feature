Feature: View the book catalog
  As a User
  I want to see the catalog of books
  So that I can browse available books

  Scenario: The catalog loads with a list of books
    Given User open the reading list application
    Then User should see a list of books
    And at least one book should be visible
