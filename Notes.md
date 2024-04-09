# Automated Apartment Availability Monitoring with Python and GCP

A short description about the project and/or client.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before installing the software.

* You need this
* And you need this
* Oh, and don't forget this

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ First step
$ Another step
$ Final step
```

## Usage

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

## i

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Suggestions Along the Way
#### 1. Import libraries right before using it.
This is the tips I 
#### 2. Make sure all necessary libraries are listed in 

* Live:
* Release:
* Development:

### Potential Obstacles And Solutions
Here is a list of problems I faced during coding under local python and during Cloud Functions & Cloud Scheduler construction under GCP and actions I took to solve them.
#### Coding Construction in Python
* Master:
* Feature:
* Bugfix:
* etc...
#### Cloud Functions Creation in GCP
##### 1. Fail to pass the test run?
* First thing first, always make sure codes in main.py works well under local environment and nothing wrong with the code
* Check if the "Entry point" is the first function/step your whole coding starts with; for example, here, you defined three functions, you should not just leave them there but add another code of main() to perform the whole task thus "Entry point" = main
* Check if all extra libraries and their versions are written under requirements.txt; Specifically under this apartment case, the version of beautifulsoup4 does not need to be specified as it works well when just leave it there thus it looks like:
  1. functions-framework==3.*
  2. requests == 2.31.0
  3. beautifulsoup4

#### CLoud Scheduler Creation in GCP

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
