# PTPTG
Python Test PlayGround, not PTPTN

- [PTPTG](#ptptg)
  - [Purpose](#purpose)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Test Strategy](#test-strategy)
  - [Setting Up Virtual Environment](#setting-up-virtual-environment)
  - [Running The Tests...](#running-the-tests)
  - [Resources](#resources)
    - [Google Cloud Platform, Functions Framework](#google-cloud-platform-functions-framework)

## Purpose

Serves as self note and guidance for implementing Unit Test and Integration Test for Python Scripts or Projects involves Google Cloud Platform. 

The idea, is to produce robust testing example for professionals like me.

## Objective

1) Write Unit and Integration tests
2) Run tests in different environment
3) Proper Python structure
4) Testable Functions

## Requirements

* Python 3.x
* pytest
* virtualenv

## Test Strategy

* Storage Triggered Functions
  * Test if it gets triggered

## Setting Up Virtual Environment

Inside the project, run this:
```
python -m venv env
```

Explanation:
```
python<version> -m venv <virtual-environment-name>
```

## Running The Tests...

Remember! Be sure that you have pytest (Python testing framework) installed, with:

```
pip3 install pytest
```

Then just run this in the terminal from the project root path for example:
```
pytest
```

## Resources
### Google Cloud Platform, Functions Framework

Documents:  https://cloud.google.com/functions/docs/functions-framework
Code: https://github.com/GoogleCloudPlatform/functions-framework-python