# qBay - Python-CI-2021

[![Pytest-All](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml/badge.svg)](https://github.com/KarlDorogy/Cisc-327-Course-Project-Group-20/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml/badge.svg)](https://github.com/KarlDorogy/Cisc-327-Course-Project-Group-20/actions/workflows/style_check.yml)

This folder contains the qbay folder structure:

```
├── LICENSE
├── README.md
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                 ======> Application source code
│   ├── __init__.py      ======> Required for a python module
│   ├── __main__.py      ======> Program entry point
│   ├── controllers.py   ======> Program html web page post and get request controller
│   ├── models.py        ======> Data models
│   └── templates        ======> Folder for frontend web page testing
│       ├── base.html               ======> default base template for all other html web pages to insert into
│       ├── createproduct.html      ======> html web page for user to create a product
│       ├── index.html              ======> html home web page for users
│       ├── login.html              ======> html web page for user to login into a account
│       ├── register.html           ======> html web page for user to register an account 
│       ├── updateproduct.html      ======> html web page for user to update a product
│       ├── updateuser.html         ======> html web page for user to update thier account
│       └── test_update_product.py  ======> Testing code for update product web page
│
├── qbay_test            ======> Testing code
│   ├── __init__.py      ======> Required for a python module
│   ├── conftest.py      ======> Code to run before/after all the testing
│   |── test_models.py   ======> Testing code for models.py
│   └── frontend         ======> Folder for frontend web page testing
│       ├── test_1_registration.py   ======> Testing code for registration web page
│       ├── test_2_login.py          ======> Testing code for registration web page
│       ├── test_3_update_user.py    ======> Testing code for update user web page
│       ├── test_4_create_product.py ======> Testing code for create product web page
│       └── test_5_update_product.py ======> Testing code for update product web page
└── requirements.txt     ======> Dependencies
```

To run the application module (make sure you have a python environment of 3.5+)

```
$ pip install -r requirements.txt
$ python -m qbay
```

Currently it shows nothing since it is empty in the `__main__.py` file.
Database and the tables will be automatically created into a `db.sqlite` file if non-existed.

To run testing:

```
# style check (only show errors)
flake8 --select=E .  

# run all testing code 
pytest -s qbay_test

```