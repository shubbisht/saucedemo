# SauceDemo UI Automation Framework

## Overview

This project contains UI automation tests for the SauceDemo application using:

- Python
- Playwright
- Pytest
- Page Object Model (POM)

The framework is designed to be readable, reusable, and easy to maintain.

---

## Project Structure

```
saucedemo/
│
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_sort.py
│
├── test_Data/
│   ├── credentials.py
│   └── checkout_data.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.12+
- Playwright

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Running Tests

Run all tests:

```bash
pytest
```
The HTML report will be generated at:

```text
Reports/report.html
```

Run a specific test:

```bash
pytest tests/test_login.py
```

Run with verbose output:

```bash
pytest -v
```

---

## Test Scenarios Covered

### Login

- Standard user can log in successfully.
- Locked-out user receives the correct error message.

### Cart

- Add two products to the cart.
- Verify the cart badge updates correctly.

### Checkout

- Complete the checkout process.
- Verify the order confirmation message.

### Sorting

- Sort products by Price (Low to High).
- Verify the products are displayed in ascending price order.

---

## Framework Features

- Page Object Model (POM)
- Reusable page methods
- Test data separation
- Independent test execution
- Readable assertions
- Playwright semantic locators

---

## Author

Shub Bisht