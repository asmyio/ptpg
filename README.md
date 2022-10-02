# PTPTG
Python Test PlayGround, not PTPTN

- [PTPTG](#ptptg)
  - [Purpose](#purpose)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Test Strategy](#test-strategy)
  - [Setting Up Virtual Environment](#setting-up-virtual-environment)
      - [A) Mac](#a-mac)
      - [B) Windows](#b-windows)
  - [Checking your Virtual Environment](#checking-your-virtual-environment)
  - [Requirement File!](#requirement-file)
  - [Running The Tests...](#running-the-tests)
    - [Deactivating Virtual Environment](#deactivating-virtual-environment)
  - [Resources](#resources)
    - [Google Cloud Platform, Functions Framework](#google-cloud-platform-functions-framework)
    - [Pytest](#pytest)
    - [Venv](#venv)
  - [Author](#author)

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

Inside the project, run this to generate a couple of files:

```
python -m venv env
```
Explanation:
```
python<version> -m venv <virtual-environment-name>
```

then, from the root of your project, based on your OS:

#### A) Mac
```
source env/bin/activate
```
#### B) Windows

CMD:
```
 env/Scripts/activate.bat
 ```
 Powershell:
 ```
 env/Scripts/Activate.ps1
 ```

this activates the environment as you can see at the left of your terminal with (env).

REMINDER: DON'T FORGET TO PUT YOUR ENV DIRECTORY IN .gitignore file

just open up .gitignore file and add 

```
env/
```

that is it! It can be easily replicated in any new environment anyway ¯\_(ツ)_/¯

## Checking your Virtual Environment

```
pip list
```

You'll see the list of packages that are installed within the virtual environment, if something's missing (as it is supposed to be*), then you'd better move on to the next step, requirement file :)

*we're in a virtual environment, of course the previous libraries you've already have is not a part of them :)

## Requirement File!

Create a requirement file like dev_requirements.txt or requirements_dev.txt however you like. Why? Because we don't wanna mix things when deploying to Google Cloud Functions via Serverless for example, and put the lists of things that the script/program requires in order for it to run.

Just for reference, here is what requirements_dev.txt contains:

```
numpy
pandas
json
```

and save it as inside the root folder of your application, once you're done. Run this:

```
pip3 install -r requirements_dev.txt
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
### Deactivating Virtual Environment

Simply run this in your terminal

```
deactivate
```

and... done, you're back. Can see that (env) is finally gone :)

## Resources
### Google Cloud Platform, Functions Framework

Documents:  https://cloud.google.com/functions/docs/functions-framework
Code: https://github.com/GoogleCloudPlatform/functions-framework-python

### Pytest

Documents: https://docs.pytest.org/

### Venv

Documents: https://docs.python.org/3/library/venv.html

## Author

[Ahmad Siraj MY](https://linkedin.com/in/asmyio)