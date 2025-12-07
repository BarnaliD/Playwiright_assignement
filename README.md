# Reading List Test Automation

Automated testing suite for the Reading List web application using Python, Playwright, and Behave (BDD).

## What Has Been Tested

This project tests the following functionality of the Reading List application:

### Features Tested
1. **View Catalog** - Users can view the list of available books
2. **Favorite Books** - Users can mark books as favorites
3. **Unfavorite Books** - Users can remove books from favorites
4. **Add New Books** - Users can add new books to the catalog
5. **Navigate to Add a Book** - Users  navigate to add a book Page

### Test Coverage
- All main user workflows
- Navigation between pages
- Form submissions
- State persistence (favorites)
- UI element visibility and interactions

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME


2. Create a virtual environment:

python -m venv .venv


3. Activate the virtual environment:
   - **Windows:**

     .\.venv\Scripts\Activate.ps1

   - **Mac/Linux:**

     source .venv/bin/activate


4. Install dependencies:

pip install -r requirements.txt


5. Install Playwright browsers:

playwright install chromium


## Running Tests

### Run all tests:

behave


### Run a specific feature:

behave features/view_catalog.feature


### Run with visible browser (for debugging):
Edit `features/environment.py` and change `headless=True` to `headless=False`, then run:

behave


### Run with detailed output:

behave --no-capture

## Project Structure

├── features/
│   ├── environment.py           # Test hooks and browser setup
│   ├── view_catalog.feature     # Catalog viewing tests
│   ├── favorite_book.feature    # Favorite functionality tests
│   ├── unfavorite_book.feature  # Unfavorite functionality tests
│   ├── add_a_book.feature       # Add book tests
│   ├── navigate_add_book.feature       # Navigation tests
│   └── steps/
│       ├── view_catalog_steps.py
│       ├── favorite_book_steps.py
│       ├── unfavorite_book_steps.py
│       ├── add_a_book_steps.py
│       └── navigate_add_book_steps.py
├── requirements.txt
├── README.md
├── STORIES.md
└── .gitignore


## Technologies Used

- **Python 3.x** - Programming language
- **Playwright** - Browser automation
- **Behave** - BDD framework for Python
- **Git/GitHub** - Version control

## Application Under Test

- **URL:** https://tap-vt25-testverktyg.github.io/exam--reading-list/
- **Type:** React-based reading list management application

## Author

Barnali Mohanty