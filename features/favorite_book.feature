Feature: Favorite a book
  As a user
  I want to mark a book as a favorite
  So that I can easily find it later

  Scenario: User favorites a book from the catalog
    Given User goes to the reading list application
    When User clicks the favorite button on a book
    Then The book should be marked as favorite
    And The book should appear in the favorites list