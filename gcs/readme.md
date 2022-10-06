# Testing Google Cloud Storage

- [Testing Google Cloud Storage](#testing-google-cloud-storage)
  - [Requirements](#requirements)
  - [Initial Setup](#initial-setup)
    - [1: Initializing Python Environment](#1-initializing-python-environment)
      - [Activating virtual env on Mac](#activating-virtual-env-on-mac)
      - [Activating virtual env on Windows](#activating-virtual-env-on-windows)
    - [2: Install the dependencies](#2-install-the-dependencies)
    - [3: Setting Up Google Cloud SDK](#3-setting-up-google-cloud-sdk)
    - [4: Setting Up gcloud Default-Credentials](#4-setting-up-gcloud-default-credentials)
  - [Running the test](#running-the-test)
  - [Exiting the virtual environment](#exiting-the-virtual-environment)
  - [Setting up the GitHub Action](#setting-up-the-github-action)
  - [Reference](#reference)
  - [Author](#author)


## Requirements

- gcloud: https://cloud.google.com/sdk/gcloud
- google cloud storage: https://pypi.org/project/google-cloud-storage/
- pytest: http://pytest.org
- pyenv: https://virtualenv.pypa.io/en/latest/

## Initial Setup

### 1: Initializing Python Environment

```
python -m venv env
```

Explanation:

```
python<version> -m venv <virtual-environment-name>
```

then, depending on the Operating System that you're on, activate it

#### Activating virtual env on Mac

in the terminal at the root project

```
source env/bin/activate
```

#### Activating virtual env on Windows

in the terminal at the root project

For CMD:
```
 env/Scripts/activate.bat
```

For Powershell:
```
env/Scripts/Activate.ps1
```

### 2: Install the dependencies

```
pip3 install -r requirements.txt
pip3 install -r requirements_dev.txt
```

### 3: Setting Up Google Cloud SDK

In order to test the google cloud storage in the local machine, or github action, we would need to authorize the gcloud to access Google Cloud using an existing service account while also specifying a project.

Authorize the Google Cloud

```
gcloud auth activate-service-account SERVICE_ACCOUNT@DOMAIN.COM --key-file=/path/key.json --project=PROJECT_ID
```
- Replace SERVICE_ACCOUNT@DOMAIN.COM with the GCP service account email.

- Replace the /path/key.json with the downloaded secrets or copied secrets from confluence.

- Replace PROJECT_ID with the GCP project

### 4: Setting Up gcloud Default-Credentials

When we are developing code that would normally use a service account but need to run the code in a local development environment where it's easier to provide user credentials. 

```
gcloud auth application-default login --client-id-file=clientid.json
```

create the client ID here: https://console.cloud.google.com/apis/credentials and grab the JSON then replace the path for clientid.json in the command

## Running the test

After initializing the setup, run pytest as usual:

```
pytest
```

## Exiting the virtual environment

```
deactivate
```

and there you have it.

## Setting up the GitHub Action

- Follow all the instrucions above
- Within the workflow
- Replace the environment with environment variable

Read more here: https://docs.github.com/en/actions/learn-github-actions/environment-variables

## Reference

Python Storage API: https://github.com/googleapis/python-storage

## Author

[Ahmad Siraj MY](https://linkedin.com/in/asmyio)