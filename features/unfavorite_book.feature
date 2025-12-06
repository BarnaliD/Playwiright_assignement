Feature: Unfavorite a book
  As a user
  I want to remove the favorite mark from the book
  So that I can delte the bbok from favorite list

Scenario: The catalog loads with a list of books
    Given User clicks on the reading list application
    And User has favorited a book
    When User clicks the favorite button again
    Then The book should be removed from favorites
