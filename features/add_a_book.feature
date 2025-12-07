Feature: Add a book to the cataloge
As a user  
I want to submit a new book with title  
So that it appears in the catalog  

Scenario: User adds a new book successfully
    Given User is on the application page
    When User clicks on the button for adding the book
    And User fills in the book details
    And User submits the book form
    Then The new book should appear in the catalog