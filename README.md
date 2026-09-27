# Selenium Python Automation Framework

## Project Overview

This project is a Selenium-based web automation framework developed in
Python for automating the **Login** and **Product Search**
functionalities of an e-commerce application.

The framework is designed using:

-   Python
-   Selenium WebDriver
-   PyTest
-   Python Unittest
-   Page Object Model (POM)
-   CSV-based test data
-   Configuration management
-   Reusable utility classes
-   Failure screenshots
-   Logging
-   HTML test reporting

The application used for automation is **Automation Exercise**, a
practice e-commerce website. Its official test cases include a
valid-login flow and a product-search flow that match the objectives of
this project.

## Project Objective

> Automate the Login and Product Search functionality of an E-Commerce
> application using a scalable framework.

### Automated Functionalities

#### 1. Login

The framework automates:

1.  Launch the browser.
2.  Open the Automation Exercise website.
3.  Click **Signup / Login**.
4.  Enter the registered email address.
5.  Enter the password.
6.  Click **Login**.
7.  Verify that the user is logged in successfully.

The framework also contains a negative login test using invalid
credentials and verifies the login error message.

#### 2. Product Search

The framework automates:

1.  Launch the browser.
2.  Open the Automation Exercise website.
3.  Navigate to **Products**.
4.  Enter a product name in the search box.
5.  Click **Search**.
6.  Verify that **Searched Products** is displayed.
7.  Verify that search results are present.

These flows correspond to the website's documented Login and Search
Product test cases.

## Framework Architecture

``` text
                    TEST CASES
                        |
              +---------+---------+
              |                   |
            PyTest             Unittest
              |                   |
              +---------+---------+
                        |
                  PAGE OBJECTS
                        |
          +-------------+-------------+
          |             |             |
      HomePage       LoginPage     SearchPage
          |             |             |
          +-------------+-------------+
                        |
                    BasePage
                        |
                  Selenium WebDriver
                        |
                      Chrome
                        |
               Automation Exercise
```

## Project Structure

``` text
API_test_Automation_selenium/
│
├── config/
│   ├── __init__.py
│   └── config.ini
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_product_search.py
│   └── unittest_login.py
│
├── test_data/
│   ├── __init__.py
│   └── test_data.csv
│
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── screenshot.py
│   └── logger.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Components

### Page Object Model

The Page Object Model separates page-specific locators and actions from
the test cases.

-   `BasePage` contains reusable Selenium operations such as click,
    enter text, wait, and retrieve text.
-   `HomePage` contains actions available from the home page.
-   `LoginPage` contains login-related locators and actions.
-   `SearchPage` contains product-search-related locators and actions.

This reduces duplicated Selenium code and makes maintenance easier when
the UI changes.

### PyTest

PyTest is the primary test runner.

Tests can be executed with:

``` bash
python -m pytest -v
```

### Unittest

A separate Unittest test is included to demonstrate the use of Python's
built-in `unittest` framework.

Run it with:

``` bash
python -m unittest tests.unittest_login
```

### Fixtures

`conftest.py` contains the PyTest `driver` fixture.

The fixture:

1.  Reads the browser configuration.
2.  Creates the WebDriver.
3.  Provides the driver to the test.
4.  Closes the browser after the test.

### Configuration Management

`config/config.ini` stores configuration values such as:

``` ini
[DEFAULT]
base_url = https://automationexercise.com
browser = chrome
implicit_wait = 10
explicit_wait = 10
```

This avoids hard-coding environment-specific values throughout the test
cases.

### CSV Test Data

Test data is stored separately in:

``` text
test_data/test_data.csv
```

Example:

``` csv
test_case,email,password,product
valid_login,test@example.com,test_password,Blue Top
invalid_login,invalid@example.com,wrongpassword,Blue Top
search_product,test@example.com,test_password,Blue Top
```

Use a dedicated test account for valid-login testing. Do not commit real
personal passwords or secrets to a public repository.

### Screenshots on Failure

The framework contains a screenshot utility.

When a test fails inside the protected test flow, the framework can
capture the current browser screen and save it under:

``` text
screenshots/
```

### Logging

The logging utility writes execution information to:

``` text
logs/test_execution.log
```

Logs can be used to understand which stage of a test was reached before
a failure.

### HTML Reporting

PyTest HTML is used to generate an execution report.

``` bash
python -m pytest --html=reports/report.html --self-contained-html
```

The report contains the test execution results in an HTML format.

## Technologies and Dependencies

The main dependencies are:

``` text
selenium
pytest
pytest-html
```

The project may also use `webdriver-manager` if explicit ChromeDriver
management is retained in `driver_factory.py`.

Python standard-library modules such as:

-   `unittest`
-   `csv`
-   `configparser`
-   `logging`
-   `os`
-   `datetime`

do not need to be installed using pip.

## Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd API_test_Automation_selenium
```

### 2. Create a virtual environment

On Windows:

``` bash
python -m venv .venv
```

### 3. Activate the virtual environment

``` bash
.venv\Scripts\activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

## Running the Tests

### Run all PyTest tests

Run the command from the **project root**:

``` bash
python -m pytest -v
```

### Run only Login tests

``` bash
python -m pytest tests/test_login.py -v
```

### Run only Product Search

``` bash
python -m pytest tests/test_product_search.py -v
```

### Run Unittest

``` bash
python -m unittest tests.unittest_login
```

### Generate HTML report

``` bash
python -m pytest --html=reports/report.html --self-contained-html
```

## Important: How to Run the Framework

Run PyTest from the project root:

``` text
C:\Users\purba\Desktop\API_test_Automation_selenium>
```

Use:

``` bash
python -m pytest -v
```

Avoid directly running framework test files with:

``` bash
python tests/test_login.py
```

because the framework uses project-level packages such as `pages` and
`utils`.

## Expected Test Flow

### Login

``` text
Start
  |
Open Chrome
  |
Open Automation Exercise
  |
Click Signup / Login
  |
Enter Email
  |
Enter Password
  |
Click Login
  |
Verify "Logged in as..."
  |
Pass
```

### Product Search

``` text
Start
  |
Open Chrome
  |
Open Automation Exercise
  |
Click Products
  |
Enter product name
  |
Click Search
  |
Verify "Searched Products"
  |
Verify products are displayed
  |
Pass
```

## Test Scenarios

  Test               Type       Expected Result
  ------------------ ---------- ---------------------------------------
  Valid Login        Positive   User is logged in successfully
  Invalid Login      Negative   Login error message is displayed
  Product Search     Positive   Matching search results are displayed
  Login Page Opens   Unittest   Login page is reached successfully

## Test Data and Credentials

Valid login automation requires an account that is registered on the
target application.

Do not store personal credentials, API keys, or other secrets in Git.

For a public repository, use:

-   A dedicated test account
-   Environment variables
-   A local/private configuration file
-   Or another secure secret-management method

## Failure Handling

The framework uses assertions to determine whether the expected behavior
occurred.

For example:

``` python
assert login_page.is_logged_in()
```

and:

``` python
assert search_page.is_search_results_displayed()
```

If an expected condition fails, the test fails rather than silently
continuing.

Screenshots can be captured when failures occur.

## Future Improvements

Possible future extensions include:

-   Cross-browser testing
-   More PyTest parametrization
-   Better centralized failure hooks for screenshots
-   Parallel execution
-   Jenkins CI/CD integration
-   Allure reporting
-   More e-commerce workflows such as cart and checkout
-   Environment-specific configuration
-   Secure credential management

## References

-   Automation Exercise Test Cases:
    https://www.automationexercise.com/test_cases
-   Selenium Page Object Model:
    https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
-   Selenium Python documentation:
    https://www.selenium.dev/selenium/docs/api/py/

## Author

**Purba Chakraborty**

B.Tech CSE (AIML)

2027
